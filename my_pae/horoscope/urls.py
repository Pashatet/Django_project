from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    # path('leo/', views_horoscope.leo),
    # path('aries/', views_horoscope.aries),
    # path('taurus/', views_horoscope.taurus),
    path('<int:sign_of_zodiac>/', views_horoscope.get_info_about_sign_zodiac_by_number),
    path('<str:sign_of_zodiac>/', views_horoscope.get_info_about_sign_zodiac),
]
