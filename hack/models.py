from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length= 20)
    current_price = models.IntegerField(default = 0)
    quantity_sold = models.IntegerField(default = 0)

class Family(models.Model):
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length=30)

