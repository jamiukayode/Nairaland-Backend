from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.

class User (AbstractUser):
    photo = models.ImageField(upload_to="profile")
    phone = models.CharField(max_length=20, unique = True)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]



# class test(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     email = models.EmailField(unique=True)
#     salary = models.IntegerField()
#     active = models.BooleanField(default=True)
#     photo = models.ImageField()
#     AnythingExtension =models.FileField() #e.g video audio microsoft file e.t.c
#     date = models.DateField(auto_now_add=True) # for time -timefield, for date and time = datetimefield
#     last_login = models.DateTimeField(auto_now=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     aboutme = models.TextField()