from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.TextField()
    priority=models.IntegerField()
    date=models.DateField()
    