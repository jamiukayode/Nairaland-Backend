from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Article (models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    image = models.ImageField(upload_to='post')
    other = models.ImageField(upload_to='post', default="")
    datecreated = models.DateTimeField(auto_now_add= True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    