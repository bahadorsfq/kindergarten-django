from django.shortcuts import render, get_object_or_404
from .models import ChildProfile
from .models import ActivityProgress
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import MediaReport, ChildProfile
from django.utils.safestring import mark_safe
from .models import PhotoReport
from itertools import chain
from django.db.models import Q
from .models import WeeklyTopic
from .models import FinancialRecord
from .models import FoodSchedule
from .models import KindergartenClass
import json



def public_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # یا هر صفحه‌ای که باید بعد از ورود نمایش داده شود
        else:
            return render(request, 'main/public.html', {'error': 'نام کاربری یا رمز عبور اشتباه است.'})

    return render(request, 'main/public.html')

def profile_view(request):
    child = get_object_or_404(ChildProfile, user=request.user)
    return render(request, 'main/dashboard/profile.html', {'child': child})

def gallery_view(request):
    return render(request, 'main/dashboard/gallery.html')

def food_schedule_view(request):
    return render(request, 'main/dashboard/food_schedule.html')

def weekly_topic_view(request):
    return render(request, 'main/dashboard/weekly_topic.html')

def finance_view(request):
    return render(request, 'main/dashboard/finance.html')

def logout_view(request):
    # بعداً logout واقعی می‌نویسیم، فعلاً فقط ریدایرکت به صفحه عمومی
    return render(request, 'main/public.html')

@login_required
def dashboard_view(request):
    child = ChildProfile.objects.get(user=request.user)
    return render(request, 'main/dashboard_base.html', {'child': child})
# Create your views here.

def progress_chart(request):
    activity = request.GET.get('activity', 'یوگا')

    # فیلتر براساس نام فعالیت صحیح (activity_name)
    progress_data = ActivityProgress.objects.filter(activity_name=activity).order_by('date')

    # استخراج تاریخ‌ها و امتیازها
    dates = [p.date.strftime('%Y-%m-%d') for p in progress_data]
    scores = [p.score for p in progress_data]

    context = {
        'activity_display': activity,
        'dates': json.dumps(dates, ensure_ascii=False),
        'scores': json.dumps(scores),
}
    return render(request, 'main/dashboard/progress.html', context)


@login_required
def media_gallery_view(request, media_type):
    child = ChildProfile.objects.get(user=request.user)
    class_of_child = child.kindergarten_class

    media_files = MediaReport.objects.filter(
        kindergarten_class=class_of_child,
        media_type=media_type
    ).order_by('-date')

    return render(request, 'main/report.html', {
        'media_files': media_files,
        'media_type': media_type,
    })

def weekly_topic(request):
    topic = WeeklyTopic.objects.first()  # چون فقط یک رکورد داریم
    return render(request, 'main/dashboard/weekly_topic.html', {'topic': topic})


def financial_report(request):
    child = request.user.childprofile
    records = FinancialRecord.objects.filter(child=child).order_by('-date')
    print(f"تعداد رکوردها: {records.count()}")  # برای مشاهده در لاگ سرور
    return render(request, 'main/dashboard/financial.html', {'records': records})

def food_schedule_view(request):
    food_schedule = FoodSchedule.objects.all().order_by('id')  # مرتب‌سازی به ترتیب ثبت
    return render(request, 'main/dashboard/food_schedule.html', {'food_schedule': food_schedule})


def logout_view(request):
    logout(request)
    return redirect('public_page')


