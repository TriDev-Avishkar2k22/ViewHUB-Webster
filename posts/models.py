from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Favs(models.Model):
    favid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, default='', on_delete=models.CASCADE)
    postId = models.IntegerField(default=0)