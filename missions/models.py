#from django_pg import models

from django.db import models
from django.contrib.auth.models import User

class Team (models.Model):
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    description = models.TextField
    leader = models.CharField(max_length = 20)
    members = models.TextField
    
class Customer(models.Model):
    first_name = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    citizenship = models.CharField(max_length = 40)
    
class Mission(models.Model):
    customer = models.ForeignKey('Customer')
    title = models.CharField(max_length = 30, default='DEFAULT VALUE')
    description = models.TextField
    location = models.CharField(max_length = 50)
    difficulty = models.CharField(max_length = 20)
    
    def __str__(self):
        return "Title: {0} Location: {1} Difficulty: {2}".format(self.title, self.location, self.difficulty)
    
class Report(models.Model):
    mission = models.ForeignKey('Mission')
    OUTCOME_CHOICES = (
    ('U', 'Unsuccessful'),
    ('S', 'Successful'),
)
    outcome = models.CharField(max_length = 15, choices = OUTCOME_CHOICES)
    comments = models.TextField
    
    def __str__(self):
        return self.outcome
