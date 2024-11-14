from django.db import models

class Owner(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    number_of_pets = models.IntegerField()

class Cat(models.Model):
    breed = models.CharField()
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField()
    name = models.CharField()

class Dog(models.Model):
    age = models.IntegerField()
    name = models.CharField()
    vaccinated = models.BooleanField()
    breed = models.CharField()
    description = models.TextField()

class Bird(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField()
    species = models.CharField()

class Exotic_Animal(models.Model):
    region_of_origin = models.CharField()
    name = models.CharField()
    age = models.IntegerField()
    type_of_animal = models.CharField()
    vaccinated = models.BooleanField()