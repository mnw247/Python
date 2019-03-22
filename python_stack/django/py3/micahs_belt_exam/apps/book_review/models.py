from django.db import models
from django import forms
from datetime import datetime
import re, bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        if len(postData['first_name'])<2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First Name is not long enough"
        if len(postData['last_name'])<2 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last Name is not long enough"
        if User.objects.filter(email = postData['email']):
            errors['email_exists'] = "Email is already Registered"
        if email_regex.match(postData['email']) == None:
            errors['email_format'] = "Email must be a valid format"
        if len(postData['password'])<5:
            errors['password'] = "Invalid Password! Must have no fewer than 5 characters"
        if postData['password'] != postData['verifypass']:
            errors['verifypass'] = "Password confirmation must match password."
        return errors

    def loginValidator(self, postData):
        user = User.objects.filter(email = postData['email_login']).first()
        errors = {}
        if not user:
            errors['email'] = "Please Enter Valid Email"
        elif not bcrypt.checkpw(postData['password_login'].encode('utf8'), user.password.encode('utf8')):
            errors['email'] = "Invalid Password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    comments = models.TextField(max_length=1000)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name='reviewed_books')
    book = models.ForeignKey(Book, related_name='book_reviews')

