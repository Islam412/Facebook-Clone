from django.db import models
from django.contrib.auth.models import AbstractUser



GENDER = (
    ("female", "Female"),
    ("male", "Male"),
)


class User(AbstractUser):
    full_name = models.CharField(max_length=200, null=True ,blank=True)
    user_name = models.CharField(max_length=100, null=True ,blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True, blank=True)
    
    Confirm_Password = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)


