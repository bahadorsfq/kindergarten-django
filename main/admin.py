from django.contrib import admin
from .models import ChildProfile
from .models import ActivityProgress
from .models import MediaReport
from .models import WeeklyTopic
from .models import FinancialRecord
from .models import FoodSchedule
from .models import KindergartenClass

# Register your models here.
admin.site.register(WeeklyTopic)

admin.site.register(MediaReport)

admin.site.register(ActivityProgress)

admin.site.register(FinancialRecord)

admin.site.register(KindergartenClass)

@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name']

@admin.register(FoodSchedule)
class FoodScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'breakfast', 'lunch', 'snack')


