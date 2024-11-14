from django.db import models

class Client(models.Model):
    account_type = models.CharField()
    email = models.EmailField()
    active = models.BooleanField()

class Video(models.Model):
    title = models.CharField()
    in_stock = models.IntegerField()
    rating = models.CharField()

class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    middle_int = models.CharField()
    age = models.IntegerField()

class Address(models.Model):
    street = models.CharField()
    zipcode = models.IntegerField()
    state = models.CharField()
    appt_num = models.IntegerField()

class Store(models.Model):
    name = models.CharField()
    number_of_employees = models.IntegerField()
    rating = models.FloatField()
    owner = models.IntegerField