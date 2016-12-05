from django.db import models
from softdeletes.models import SoftDeletable


class Animal(SoftDeletable, models.Model):
    CARNIVORE = 'c'
    HERIVORE = 'h'
    OMNIVORE = 'o'

    EAT_CHOICES = (
        (CARNIVORE, 'c'),
        (HERIVORE, 'h'),
        (OMNIVORE, 'o')
    )
    name = models.CharField(max_length=100)
    eats = models.CharField(max_length=50, choices=EAT_CHOICES)
    threatened = models.BooleanField(default=False)


class Jungle(SoftDeletable, models.Model):
    name = models.CharField(max_length=100)
    area = models.PositiveIntegerField()
    apex_predator = models.ForeignKey(Animal)


class AnimalInJungle(SoftDeletable, models.Model):
    animal = models.ForeignKey(Animal)
    jungle = models.ForeignKey(Jungle)
    count = models.PositiveIntegerField()
