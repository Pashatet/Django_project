from django.db import models
from  django.core.validators import MinLengthValidator

# Create your models here.

# т.к в новой форме у нас нет валидаторов их импортируем
class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    lastname = models.CharField(max_length=60, validators=[MinLengthValidator(3)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()


