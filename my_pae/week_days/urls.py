from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_info_greeting),
    path('<int:day_of_week>/', views.get_info_about_week_number_days),
    path('<str:day_of_week>/', views.get_info_about_week_days, name='day-of-week')
]
