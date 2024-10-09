from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

