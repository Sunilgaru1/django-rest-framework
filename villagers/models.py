from django.db import models

# Create your models here.

class Villager(models.Model):
    house_no = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
