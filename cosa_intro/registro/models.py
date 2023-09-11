from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade los campos adicionales que desees
    age = models.IntegerField(null=True, blank=True)
    # ...
