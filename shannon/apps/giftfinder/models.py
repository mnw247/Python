from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self,request):
        errors = {}
        if len(request['first_name']) < 2 or not  str.isalpha(request['first_name']):
            errors['first_name'] = 'first name must be at least 2 charachters long and contain no numbers'
        if len(request['last_name']) < 2 or not str.isalpha(request['last_name']):
            errors['last_name'] = 'last name must be at least 2 charachters long and contain no numbers'
        if len(request['email']) < 1 or not EMAIL_REGEX.match(request['email']):
            errors['email'] = 'must enter a vlaid email address'
        if len(request['password']) < 8:
            errors['password'] = 'pasword must be at least 8 charachters'
        if request['confirm_pw'] != request['password'] :
            errors['confirm_pw'] = 'your passwords do not match'
        return errors
    
    def jobValidator(self,request):
        errors = {}
        if len(request['title']) < 4:
            errors['title'] = "Title Must Be Greater than 3 Characters"
        if len(request['description']) < 11:
            errors['description'] = "Description Must Be Greater than 10 Characters"
        if len(request['location']) < 1:
            errors['location'] = "Location must not be blank"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255,unique=True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    
class Job(models.Model):
    title =  models.CharField(max_length = 50)
    description = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    postedon = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User,related_name="created_jobs")
    jobsadded = models.ManyToManyField(User, related_name="joined_jobs")
    objects = UserManager()
    # updated_at = models.DateTimeField(auto_now=True)