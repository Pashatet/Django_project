from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet  # для анатации QuerySet


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status', 'currency']
    #     добавляем пользователю редоктировать поля имя первого поля не указываем т.к он ссылочный и по нему мы переходим

    list_editable = ['rating', 'year', 'budget', 'currency']
    # ordering = ['rating']
    list_per_page = 5  # колисечтво выводимых результатов в таблице

    # регистрацию бд можно сделать через декоратор
    # admin.site.register(Movie, MovieAdmin)

    actions = ['ser_dollars', 'ser_euro']  # регистрируем функцию в админке

    @admin.display(ordering='name', description='Status')  # метод для создания вычисляемых полей. description делает название поля автоматом берется название метода rating_status
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'bad'
        if movie.rating < 70:
            return 'good'
        else:
            return 'well'


    # метод для создания дейсвий в админке (Action)
    @admin.action(description='Установить валюту в доллар')
    def ser_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def ser_euro(self, request, queryset: QuerySet):
        count_update = queryset.update(currency=Movie.EURO)
        self.message_user(request,
                          f'Было обновлено {count_update} записей',
                          messages.ERROR)