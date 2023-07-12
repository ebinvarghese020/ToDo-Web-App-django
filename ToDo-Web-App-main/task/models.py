from django.db import models
import datetime

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    deadline = models.DateTimeField()
    published = models.DateTimeField(default=datetime.datetime.now())
    user_id = models.IntegerField()
    completed = models.BooleanField(default=False)

