from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# Create your models here.

class Contests(models.Model):
    contest_id=models.IntegerField(blank=True,null=True)
    hacker_id=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=250 ,blank=True)

class Colleges(models.Model):
    college_id=models.IntegerField(blank=True,null=True)
    contest_id=models.IntegerField(blank=True,null=True)
    
class Challenges(models.Model):
    challenges_id = models.IntegerField(blank=True,null=True)
    college_id = models.IntegerField(blank=True,null=True)

class View_Stats(models.Model):
    challenges_id = models.IntegerField(blank=True,null=True)
    total_views=models.CharField(max_length=250,blank=True)
    total_uniqueviews=models.CharField(max_length=250,blank=True)

    

class Submission_Stats(models.Model):
    challenges_id = models.IntegerField(blank=True,null=True)
    total_submission=models.CharField(max_length=250,blank=True)
    total_accept_submission=models.CharField(max_length=250,blank=True)


class Result_Stats(models.Model):
    contest_id=models.IntegerField(blank=True,null=True)
    hacker_id=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=250 ,blank=True)
    total_views=models.CharField(max_length=250,blank=True)
    total_uniqueviews=models.CharField(max_length=250,blank=True)
    total_submission=models.CharField(max_length=250,blank=True)
    total_accept_submission=models.CharField(max_length=250,blank=True)
