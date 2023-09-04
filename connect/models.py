from PIL import Image
from django.db import models
from django.db.models import JSONField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    
    GENDER_CHOICES = [
        ('Mâle', 'male'),
        ('Femelle', 'female'),
        ('Autre', 'other'),
    ]

    
    username = models.CharField(max_length=150, unique=True)

    email = models.EmailField(
        ("email address"), unique=True, blank=True, null=True, default=None)

    phone_number = models.CharField(
        max_length=17, unique=True, blank=True, null=True)

    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, blank=True, null=True, default=None)

    about = models.TextField(blank=True, null=True)

    picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True, default=None)

    is_confirmed = models.BooleanField(('Is Confirmed'), default=False)

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def save(self, *args, **kwargs):
        if not self.email:
            self.email = None
        if not self.phone_number:
            self.phone_number = None
        return super().save(*args, **kwargs)

