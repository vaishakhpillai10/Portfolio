from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length = 255)
    image = models.CharField(max_length=2550)
    address =models.CharField(max_length=2550)
    contact=models.IntegerField()
    email=models.CharField(max_length=2550)
    objective=models.CharField(max_length=4550)
    Skills=models.CharField(max_length=2550)
