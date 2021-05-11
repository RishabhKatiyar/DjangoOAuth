from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=True)

    def __str__(self):
        return self.username