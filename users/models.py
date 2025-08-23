from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICE = [
        ('Admin','Admin'),
        ('User',"User"),
        ]
    
    role = models.CharField(max_length=12, choices=ROLE_CHOICE, default='User')

    def __str__(self):
        return f"{self.username} {self.role}"
