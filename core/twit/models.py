from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=250,blank=True,null=True)
    last_name=models.CharField(max_length=250,blank=True,null=True)
    email=models.CharField(max_length=250,blank=True,null=True)
    phone=models.CharField(max_length=12,blank=True,null=True)
    tweets_number=models.IntegerField(default=0)
    image=models.ImageField(upload_to='profile_image')
    bio=models.TextField(blank=True,null=True)
    age=models.PositiveIntegerField(default=0,blank=True,null=True)
    city=models.CharField(max_length=250,blank=True,null=True)
    status=models.CharField(max_length=250,blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

   


class Twitter(models.Model):
    profile_user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='twitter_user')
    twit=models.CharField(max_length=250)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.twit


class Comment(models.Model):
    twitter=models.ForeignKey(Twitter,on_delete=models.CASCADE,related_name='twitter_comment')
    profiles=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='profile_comment')
    comment=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=["-updated_date"]

    

    def __str__(self):
        return self.comment   
