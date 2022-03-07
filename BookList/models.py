from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

class WriterModel(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class GenreModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class BookModel(models.Model):
    writer = models.ForeignKey(WriterModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=250)
    genres = models.ManyToManyField(GenreModel, blank=True)
    release_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
