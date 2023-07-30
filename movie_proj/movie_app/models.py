from django.db import models
from django.urls import reverse

# создание ссылки slug
from django.utils.text import slugify


# from transliterate import translit

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)

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
