from django.db import models


# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=32)
    Password=models.CharField(max_length=32)
    Con_password=models.CharField(max_length=32)
    Email=models.EmailField()
    Mob_Number=models.IntegerField

    def __str__(self):
        return self.username
