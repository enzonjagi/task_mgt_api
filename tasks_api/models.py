from django.db import models

# Create your models here.
class Data(models.Model):
    """Models for the Api data"""

    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=500)
