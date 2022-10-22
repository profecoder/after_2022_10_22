from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=40)
    model = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.model}"

class House(models.Model):
    name = models.CharField(max_length=40)
    model = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.model}"