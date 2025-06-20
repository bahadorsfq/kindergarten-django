from django.db import models
from django.contrib.auth.models import User

class KindergartenClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ChildProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    class_name = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    kindergarten_class = models.ForeignKey(KindergartenClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name
# models.py

class ActivityProgress(models.Model):
    ACTIVITY_CHOICES = [
        ('یوگا', 'یوگا'),
        ('زبان عمومی', 'زبان عمومی'),
        ('باغبانی','باغبانی'),
        ('آشپزی', 'آشپزی'),
        ('قصه خوانی', 'قصه خوانی'),
        ('سرود خوانی', 'سرود خوانی'),
        ('بارش افکار', 'بارش افکار'),
        ('بازی', 'بازی'),
        ('نقاشی', 'نقاشی'),
        ('آداب اجتماعی', 'آداب اجتماعی'),
        ('قانونمندی', 'قانونمندی'),
        ('نخ کردنی', 'نخ کردنی'),
        ('مفاهیم علوم', 'مفاهیم علوم'),
        ('کارگاه سفال', 'کارگاه سفال'),
        ('مفاهیم ریاضی', 'مفاهیم ریاضی'),
        ('کارگاه چاپ', 'کارگاه چاپ'),
        ('کاردستی', 'کاردستی'),
        ('نمایش خلاق', 'نمایش خلاق'),
        
    ]
    child = models.ForeignKey('ChildProfile', on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    score = models.IntegerField()  # مثلاً از ۰ تا ۱۰۰
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.child} - {self.activity_name}: {self.score}"

# Create your models here.
    
class MediaReport(models.Model):
    kindergarten_class = models.ForeignKey(KindergartenClass, on_delete=models.CASCADE)
    media_file = models.FileField(upload_to='media_reports/')
    media_type = models.CharField(max_length=10, choices=[('video', 'ویدئو'), ('image', 'تصویر')])
    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type} - {self.kindergarten_class.name}"


    
class PhotoReport(models.Model):
    child = models.ForeignKey('ChildProfile', on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo_reports/', blank=True, null=True)
    video = models.FileField(upload_to='video_reports/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.user.username} - {self.activity_name}"

class WeeklyTopic(models.Model):
    content = models.TextField(verbose_name="متن موضوع هفته")

    def __str__(self):
        return "موضوع هفته"

class FinancialRecord(models.Model):
    child = models.ForeignKey('ChildProfile', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='موضوع')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ')
    amount = models.PositiveIntegerField(verbose_name='مبلغ (تومان)')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده؟')

    def __str__(self):
        return f"{self.title} - {self.child.full_name}"

class FoodSchedule(models.Model):
    WEEKDAYS = [
        ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه‌شنبه', 'سه‌شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنجشنبه', 'پنجشنبه'),
        ('جمعه', 'جمعه'),
    ]

    day = models.CharField(max_length=10, choices=WEEKDAYS, unique=True)
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    snack = models.CharField(max_length=200)

    def __str__(self):
        return f"برنامه غذایی - {self.day}"


