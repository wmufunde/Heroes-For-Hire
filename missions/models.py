from django_pg import models
from django.contrib.auth.models import User


# Create your models here.
OUTCOME_CHOICES = (
    ('U', 'Unsuccessful'),
    ('S', 'Successful'),
)

STATS_CHOICES = (
    ('1', 'Extremely Low'),
    ('2', 'Very Low'),
    ('3', 'Low'),
    ('4', 'Average'),
    ('5', 'Good'),
    ('6', 'Above Average'),
    ('7', 'High'),
    ('8', 'Very High'),
    ('9', 'Super Human'),
    ('10', 'Above and Beyond'),

)
class Hero(models.Model):
    codename = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.codename
    
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
    description = models.TextField
    location = models.CharField(max_length = 50)
    difficulty = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.description, self.location, self.difficulty
    
    
class Alias(models.Model):
    hero = models.ForeignKey('Hero')
    first_name = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 30)
    former_codenames = models.TextField
    occupation = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    citizenship = models.CharField(max_length = 30)
    
class HeroStats(models.Model):
    hero = models.ForeignKey('Hero')
    height = models.CharField(max_length = 10)
    weight = models.CharField(max_length = 10)
    powers = models.TextField
    intelligence = models.CharField(max_length = 5, choices = STATS_CHOICES)
    stamina = models.CharField(max_length = 5, choices = STATS_CHOICES)
    strength = models.CharField(max_length = 5, choices = STATS_CHOICES)

class HeroStatus(models.Model):
    hero = models.ForeignKey('Hero')
    hero = models.IntegerField
    mission = models.IntegerField
    team = models.IntegerField
    
    def __str__(self):
        return "{0} is registered in team {1}, and is currenly on mission {3}".format(self.hero, self.team, self.mission) 
    
class Report(models.Model):
    mission = models.ForeignKey('Mission')
    outcome = models.CharField(max_length = 15, choices = OUTCOME_CHOICES)
    comments = models.TextField
    
    def __str__(self):
        return self.outcome
