from idlelib.pyparse import trans

from django.db import models
from django.utils.timezone import datetime
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255, default='')
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

