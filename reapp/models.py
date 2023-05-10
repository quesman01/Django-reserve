# models.py
from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    # num_guests = models.IntegerField()

    def __str__(self):
        return self.name

