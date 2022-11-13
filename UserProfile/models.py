from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from home.models import upload

class Playlist(models.Model):
    Name = models.CharField(max_length=30, default='New Playlist')
    description = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, null=False, default='', on_delete=models.CASCADE)
    list_post = models.ManyToManyField(upload, related_name='playlist')
    playId = models.AutoField(primary_key=True)