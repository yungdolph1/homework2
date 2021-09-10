from django.contrib import admin
from .models import MyFirstModel, MySecondModel

# Register your models here.

admin.site.register(MyFirstModel)
admin.site.register(MySecondModel)

