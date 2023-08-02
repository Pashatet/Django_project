from django.db import models
from django.urls import reverse

# создание ссылки slug
from django.utils.text import slugify


# метод для волидирования полей
from django.core.validators import MaxValueValidator,MinValueValidator

# from transliterate import translit

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100, default='top player')
    director_email = models.EmailField(default='top_player@top.gun')

    def get_url(self):
        return reverse('one_dir', args=[self.id])

    def __str__(self):
        return f'{self.first_name} {self.director} {self.director_email}'


class Actor(models.Model):
    first_name = models.CharField(max_length=100, default='First name')
    last_name = models.CharField(max_length=100, default='Last name')
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Man'),
        (FEMALE, 'Women'),
    ]
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)


    def __str__(self):
        if self.gender == self.MALE:
            return f' Актер {self.first_name} {self.last_name}'
        else:
            return f' Актриса {self.first_name} {self.last_name}'

class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True) #blank для хранения пустых значений в поле admin
    budget = models.IntegerField(default=1000000)

    # создаем foreignKey null=True для возможности сохранения пустых значений PROTECT не позволяет удалить значение
    # пока на него ссылается поле(когда у него есть дочерние записи)
    # on_delete=models.CASCADE при попытке удаления поля удалятся записи связанные с этим полем
    # on_delete=models.SET_NULL при таком удалении поля в записях связаных с этим поле проставится значение null
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)


    slug = models.SlugField(default='', null=False, db_index=True)
    # Choices field https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-choices применяется когда у нас маленький выбор значений
    EURO = 'EUR'
    USD = 'UDS'
    RUB = 'RUB'
    CORRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    currency = models.CharField(max_length=3, choices=CORRENCY_CHOICES, default=RUB)

    def save(self, *args, **kwargs):
        # slug_url = translit(self.last_name + self.firs_name, language_code='ru', reversed=True)
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    # функция для постоения ссылки
    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

# from movie_app.models import Movie
