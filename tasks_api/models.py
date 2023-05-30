from django.db import models

# Create your models here.
class Data(models.Model):
    """Models for the Api data"""

    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True,
    )
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        self.task_name
