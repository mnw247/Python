from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField(max_length=255)
    def __repr__(self):
        return f'Dojo(id={self.id},name={self.name},city={self.city}, state={self.state})'

class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    dojo_name = models.ForeignKey(Dojo, related_name="ninjas")
    def __repr__(self):
        return f'Ninja(id={self.id},first_name={self.first_name},last_name={self.last_name},state={self.state}, dojo_name={self.dojo_name})'