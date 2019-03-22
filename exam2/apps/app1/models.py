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
    
    def editValidator(self,request):
        errors = {}
        user=User.objects.filter(email=request['email'])
        if len(request['first_name']) < 2 or not  str.isalpha(request['first_name']):
            errors['first_name'] = 'first name must be at least 2 charachters long and contain no numbers'
        if len(request['last_name']) < 2 or not str.isalpha(request['last_name']):
            errors['last_name'] = 'last name must be at least 2 charachters long and contain no numbers'
        if len(request['email']) < 1 or not EMAIL_REGEX.match(request['email']):
            errors['email'] = 'must enter a valid email address'
        if request['email'] != User.objects.get(id=request['id']).email:
            if user:
                errors['email_taken'] = "This email is already being used"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255,unique=True)
    password = models.CharField(max_length = 255)
    objects = UserManager()

class Quote(models.Model):
    author = models.CharField(max_length = 255)
    message = models.TextField()
    created_by = models.ForeignKey(User, related_name="quote_added")

class Like(models.Model):
    user = models.ForeignKey(User, related_name="liked_quote")
    quote = models.ForeignKey(Quote, related_name="quote_liked")