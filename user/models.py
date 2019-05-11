from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.username