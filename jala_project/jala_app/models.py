from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

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
    mobile_number = models.CharField(max_length=10)
    # mobile_number = PhoneNumberField(region='IN')   
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    other_city = models.CharField(max_length=100, blank=True, null=True)
    skills = models.CharField(max_length=299, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
