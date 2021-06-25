from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    pen_name=models.CharField(max_length=100,unique=True)
    
    
class books(models.Model):
    author_id = models.ForeignKey(authors,on_delete=models.CASCADE,db_column='author_id')
    title=models.CharField(max_length=100)
    year=models.CharField(max_length=100)

    