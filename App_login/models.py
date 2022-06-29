from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

gender_choice = (
    ('male', 'Male'),
    ('Female', 'Female'),
    ('Third Gender', 'Third Gender')
)


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='photos/profile_picture')
    phone_number = models.CharField(max_length=14)
    gender = models.CharField(choices=gender_choice, max_length=12)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.username}'
