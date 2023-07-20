from django.urls import path, register_converter
# from . import views as views_horoscope
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')


urlpatterns = [
    path('', views.index),
    path('<my_date:sign_of_zodiac>', views.get_my_date_converters),
    path('<yyyy:sign_of_zodiac>', views.get_yyyy_converters),
    path('type/', views.type_index),
    path('type/<str:type_of_name>/', views.type_horoscope),
    path('<int:sign_of_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_of_zodiac>', views.get_my_float_converters),
    path('<str:sign_of_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
