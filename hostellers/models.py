from django.db import models

# Create your models here.
class Hosteller(models.Model):
    hostel_no = models.PositiveIntegerField()
    room_no = models.PositiveIntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
