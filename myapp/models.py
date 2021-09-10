from django.db import models

# Create your models here.

class MyFirstModel(models.Model):
    name = models.CharField(max_length=45)
    number = models.IntegerField(default=0)

class MySecondModel(models.Model):
    name = models.ForeignKey(to=MyFirstModel, default=0,on_delete=models.SET_DEFAULT)