from django.urls import path
from . import views as views_geometry

urlpatterns = [
    path('get_rectangle_area/''<int:width>/''<int:height>/', views_geometry.get_info_about_rectangle_area2),
    path('rectangle/''<int:width>/''<int:height>/', views_geometry.get_info_about_rectangle_area),
    path('square/''<int:width>/', views_geometry.get_info_about_square_area),
    path('circle/''<int:radius>/', views_geometry.get_info_about_circle_area),
]
