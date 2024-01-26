from django.db import models
from django.contrib.auth.models import AbstractUser


from PIL import Image
from shortuuid.django_fields import ShortUUIDField


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

    # Change defult django in adminbanal
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)




RELATIONSHIP = (
    ("single","Single"),
    ("married","married"),
    ("inlove","In Love"),
)





class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_images = models.ImageField(upload_to='Images')
