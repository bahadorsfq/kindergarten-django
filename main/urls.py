from django.urls import path
from . import views
from .views import financial_report
urlpatterns = [
    path('', views.public_page, name='public_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('media/<str:media_type>/', views.media_gallery_view, name='media_gallery'),
    path('dashboard/profile/', views.profile_view, name='profile'),
    path('dashboard/progress/', views.progress_chart, name='progress'),
    path('dashboard/gallery/', views.gallery_view, name='gallery'),
    path('dashboard/food/', views.food_schedule_view, name='food_schedule'),
    path('dashboard/topic/', views.weekly_topic_view, name='weekly_topic'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/weekly_topic/', views.weekly_topic, name='weekly_topic'),
    path('dashboard/financial/', financial_report, name='financial'),
]
