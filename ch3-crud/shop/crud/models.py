from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    qty=models.CharField(max_length=100)