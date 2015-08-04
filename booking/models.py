from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Booking(models.Model):
    place = models.ForeignKey(Place)
    person = models.ForeignKey(Person)
    # time = models.
