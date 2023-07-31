from django.contrib import admin
from .models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget']
#     добавляем пользователю редоктировать поля имя первого поля не указываем т.к он ссылочный и по нему мы переходим

    list_editable = ['rating', 'year', 'budget']
    ordering = ['rating']
    list_per_page = 5 # колисечтво выводимых результатов в таблице

# регистрацию бд можно сделать через декоратор
# admin.site.register(Movie, MovieAdmin)
