from __future__ import unicode_literals
from django.db import models


class User (models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f'User(id={self.id},first_name={self.first_name},last_name={self.last_name}, email={self.email}, age={self.age})'