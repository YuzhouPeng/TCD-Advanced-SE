from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Record(models.Model):
    record_time = models.DateTimeField('date published')
    remark = models.CharField(max_length=200)