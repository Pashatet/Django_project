from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('type/', views_horoscope.type_index),
    path('type/<str:type_of_name>/', views_horoscope.type_horoscope),
    path('<int:sign_of_zodiac>/', views_horoscope.get_info_about_sign_zodiac_by_number),
    path('<str:sign_of_zodiac>/', views_horoscope.get_info_about_sign_zodiac, name='horoscope-name'),
]
