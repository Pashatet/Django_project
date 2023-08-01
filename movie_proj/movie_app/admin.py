from django.contrib import admin, messages
from .models import Movie, Director
from django.db.models import QuerySet  # для анатации QuerySet


# для создания собственного филттра нужно создать новый класс
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 70', 'Сведний'),
            ('>=70', 'Высокий'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == 'от 40 до 70':
            return queryset.filter(rating__gte=40).filter(rating__lt=70)
        elif self.value() == '>=70':
            return queryset.filter(rating__gte=70)


# Register your models here.

admin.site.register(Director)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # добавление в пустую форму опеределенных полей через поле fields
    # fields = ['name','rating']
    exclude = ['slug'] # исключение опеределенных полей с пустой формы
    readonly_fields = ['year'] # запретить пользователю редактировать опеределенные поля в пустой форме
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status', 'currency']
    #     добавляем пользователю редоктировать поля имя первого поля не указываем т.к он ссылочный и по нему мы переходим

    list_editable = ['rating', 'year', 'budget', 'currency']
    # создание автоматического slug
    prepopulated_fields = {'slug': ('name',)}

    # ordering = ['rating']
    list_per_page = 5  # колисечтво выводимых результатов в таблице

    # регистрацию бд можно сделать через декоратор
    # admin.site.register(Movie, MovieAdmin)

    actions = ['ser_dollars', 'ser_euro']  # регистрируем функцию в админке
    # создание поискового поля
    search_fields = ['name']
    # добавление фильтрации
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='name',
                   description='Status')  # метод для создания вычисляемых полей. description делает название поля автоматом берется название метода rating_status
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
