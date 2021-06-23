from django.db import models

# Create your models here.
class Data(models.Model):
    number1=models.IntegerField(default=0)
    number2=models.IntegerField(default=0)

    def __str__(self):
        return self.number1