from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    gender = (
        ('male',"Male"),
        ('female',"Female"),
        ('other',"Other"),
    )
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    sex = models.CharField(max_length=32, choices=gender, default='Male')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-create_time"]
        verbose_name = "user"
        verbose_name_plural = "user"

class Record(models.Model):
    username = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    record_time = models.DateTimeField('date published')
    remark = models.CharField(max_length=200)


class SystemUser(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)