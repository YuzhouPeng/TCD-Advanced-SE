from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
