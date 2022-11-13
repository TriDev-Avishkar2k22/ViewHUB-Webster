from email.policy import default
from msilib.schema import File
from secrets import choice
from sqlite3 import Timestamp
from urllib import request
import uuid
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
from home.validators import fileSize



class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=200)
    is_verfied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# # Create your models here.
# class Signup(models.Model):
#     fname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=50)
#     email = models.CharField(max_length=30)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     Time = models.TimeField(auto_now_add=True,blank=True)

#     def __str__(self):
#         return 'signup of' + self.fname

class upload(models.Model):

    TAGS_CHOICES = (
        ('Film & Animation', 'Film & Animation'),
        ('Autos & Vehicles','Autos & Vehicles'),
        ('Music','Music'),
        ('Pets & Animals','Pets & Animals'),
        ('Sports','Sports'),
        ('Travel & Events','Travel & Events'),
        ('Gaming','Gaming'),
        ('People & Blogs','People & Blogs'),
        ('Comedy','Comedy'),
        ('Entertainment','Entertainment'),
        ('News & Politics','News & Politics'),
        ('Howto & Style','Howto & Style'),
        ('Education','Education'),
        ('Science & Technology','Science & Technology'),
        ('Nonprofits & Activism','Nonprofits & Activism')
    )

    Title = models.CharField(max_length=100)
    file = models.FileField(upload_to='', validators=[fileSize])
    upload_author = models.ForeignKey(User, on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    postId = models.AutoField(primary_key=True)
    isfav = models.BooleanField(default=0)
    private = models.BooleanField(default=0)
    Tag = models.CharField(max_length=50, choices=TAGS_CHOICES, default='Web_Development')

    def __str__(self):
        return self.Title
# class Comments(models.Model):
#     # username = models.ForeignKey(Users, on_delete=models.CASCADE) 
#     video = models.ForeignKey(Post, on_delete=models.CASCADE)
#     describe = models.TextField(null=True)
#     post_date = models.DateTimeField(blank=True, auto_now=True)
    
#     def __str__(self):
#         self.save()
#         return 'Comment %s by %s'%(self.describe, self.username)
class contact(models.Model):
    Name = models.CharField(max_length=50)
    Issue = models.TextField()
    query_related = models.CharField(max_length=13)
    Email = models.CharField(max_length=100)
    Time = models.TimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return  'Message from ' + self.Name
