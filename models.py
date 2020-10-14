from django.db import models

class Person(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

class Personset(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name