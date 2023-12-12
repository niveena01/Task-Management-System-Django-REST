from django.db import models


# Create your models here.
class TaskModel(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    images = models.ImageField(upload_to='images/', default="Image/None/Noimg.jpg")


def __str__(self):
    self.task_name
