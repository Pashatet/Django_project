from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    # path('movie/<int:id_movie>', views.show_one_movie, name='movie-detail'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_directors, name='all-directors'),
    path('directors/<int:id_dir>', views.one_dir, name='one-directors'),
    path('actors/', views.all_actors, name='all-actors'),
    path('actors/<int:id_actor>', views.one_actor, name='one-actor'),
]
