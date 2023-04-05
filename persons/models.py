from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    favorite_colors = models.ManyToManyField("Color")


class Color(models.Model):
    name = models.CharField(max_length=100)
