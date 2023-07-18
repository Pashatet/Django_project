from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('<int:day_of_week>/', views_horoscope.get_info_about_week_number_days),
    path('<str:day_of_week>/', views_horoscope.get_info_about_week_days),
]
