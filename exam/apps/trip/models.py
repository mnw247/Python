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
    
    def tripValidator(self,request):
        errors = {}
        today = datetime.now()
        if len(request['destination']) < 1:
            errors['destination'] = "No Destination Typed"
        if len(request['description']) < 1:
            errors['description'] = "No Description Typed"
        if len(request['sdate']) < 1:
            errors['sdate'] = "No Travel Date From Typed"
            return errors
        if len(request['edate']) < 1:
            errors['edate'] = "No Travel Date To Typed"
            return errors
        startdate = datetime.strptime(request['sdate'],'%Y-%m-%d')
        enddate = datetime.strptime(request['edate'],'%Y-%m-%d')
        if startdate <= today:
            errors['sdate'] = "Start Date is Invalid"
        if enddate <= startdate:
            errors['edate'] = "End Date must be after Start Date"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255,unique=True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    
class Trip(models.Model):
    destination =  models.CharField(max_length = 50)
    description = models.TextField(max_length=100)
    sdate = models.DateField()
    edate = models.DateField()
    creator = models.ForeignKey(User,related_name="created_trips")
    trip_members = models.ManyToManyField(User, related_name="joined_trips")
    objects = UserManager()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)