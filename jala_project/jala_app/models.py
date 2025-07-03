from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

SKILL_CHOICES = [
    ('AWS', 'AWS'),
    ('QA-Automation', 'QA-Automation'),
    ('DevOps', 'DevOps'),
    ('Full Stack Developer', 'Full Stack Developer'),
    ('Middleware', 'Middleware'),
    ('WebServices', 'WebServices'),
]

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    other_city = models.CharField(max_length=100, blank=True, null=True)
    skills = models.CharField(max_length=299)

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
