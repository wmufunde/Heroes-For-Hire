#from django.db import models
from django_pg import models
from django.contrib.auth.models import User

# Create your models here.
TRAINING_TYPE_CHOICES = (
    ('AC', 'Armed Combat'),
    ('UC', 'Unarmed Combat'),
    ('P', 'Piloting'),
    ('O', 'Other'),
)

GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('U', 'Unspecified'),
    )
OUTCOME_CHOICES = (
    ('P', 'Pass'),
    ('F', 'Fail'),
    )

class Trainer(models.Model):
    first_name = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 30)
    address = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    citizenship = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)

class Class_Training(models.Model):
    trainer = models.ForeignKey('Trainer')
    class_name = models.CharField(max_length = 30)
    type_of_class = models.CharField(max_length = 2, choices= TRAINING_TYPE_CHOICES)
    description = models.TextField(max_length = 200)
    
    def __str__(self):
            return self.class_name, self.trainer
            

class ReportLog(models.CompositeField):
    class_ID = models.IntegerField
    hero_ID = models.IntegerField
    outcome = models.CharField(max_length = 1, choices = OUTCOME_CHOICES)
    comments = models.TextField
    trainer = models.IntegerField
    
    class Meta:
        db_type = 'report'
            
class Attendance(models.CompositeField):
    class_ID = models.IntegerField
    hero_ID = models.IntegerField
    room_name = models.CharField(max_length = 30)
    date = models.DateField
    start_time = models.TimeField
    end_time = models.TimeField
        
    class Meta:
        db_type = 'attendance'
            
class Room(models.Model):
    room_name = models.CharField(max_length = 20)
    
class Hero(models.Model):
    codename = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.codename

    
