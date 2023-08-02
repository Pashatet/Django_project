from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director


# Create your views here.
def show_all_movie(request):
    # movies = Movie.objects.all()
    # movies = Movie.objects.order_by('name')
    # для полей с типом данных Null можно сделать сортировка через метод F asc - по возростанию desc - убывание nulls_[last or first]=True
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True))
    # позволяет добавлять данные в бд без ее изменения
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        new_budget=F('budget') + 100,
        false_bool=Value(False), )
    # Альтернативный спосов запистаь данные в столбец slug
    # Movie.objects.get(id=2).save() альпернативный вариант но так нужно сделать для каждой записи
    # for movie in movies:
    #     movie.save()
    agg = movies.aggregate(Sum('budget'), Avg('year'), Count('year'))

    return render(request, 'movie_app/all_movie.html', {
        "movies": movies,
        'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        "movie": movie
    })


def show_directors(request):
    directors = Director.objects.all

    return render(request, 'movie_app/director.html', {
        'directors': directors,
    })


def one_dir(request, id_dir: int):
    dir = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/one_dir.html', {
        'dir': dir
    })
