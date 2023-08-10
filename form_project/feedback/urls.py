from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view()),
    path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),
    path('list', views.ListFeedBack.as_view()),
    # pk or slug поиск осуществяется по одному из этих параметров все остальное django сделает за нас
    path("detail/<int:pk>", views.DetailFeedBack.as_view()),
]