from django.urls import path
from . import views as views_blog

urlpatterns = [
    path('', views_blog.index),
    path(route='<int:number_post>/', view=views_blog.det_info_about_post_number),
    path('<str:name_post>/', views_blog.get_info_about_post),
]