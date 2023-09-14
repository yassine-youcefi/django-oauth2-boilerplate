from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomPermission(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Custom Permission'
        verbose_name_plural = 'Custom Permission'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField(CustomPermission, related_name='roles', blank=True)

    def __str__(self):
        return self.name
     
    
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
    
    role = models.ForeignKey(Role, blank=True, null=True, related_name='users', on_delete=models.SET_NULL)
    
    custom_permissions = models.ManyToManyField(CustomPermission, related_name='users', blank=True, help_text='this field contain the user permissions')
    
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
    
    last_password_update = models.DateField(blank=True, null=True, default=None)

    last_login_ip = models.CharField(max_length=255, blank=True, null=True)
    
    last_login_lat = models.CharField(max_length=255, blank=True, null=True)
    
    last_login_long = models.CharField(max_length=255, blank=True, null=True)
    
    social_login_id = models.CharField(max_length=255, blank=True, null=True)
   
    is_confirmed = models.BooleanField(('Is Confirmed'), default=False)

    USERNAME_FIELD = 'username'
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

    def has_permission(self, url_name):
        if url_name in list(self.custom_permissions.values_list('url', flat=True)):
            return True
        return False