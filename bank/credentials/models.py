from django.db import models

class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)
class Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)

# models.py
from django.db import models

class BankAccountApplication(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    materials_required = models.BooleanField()


