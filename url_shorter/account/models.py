from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class User(models.Model):
    username = models.CharField( max_length=100, null=False)
    phone_validator = RegexValidator(regex=r'^\d{10}$', 
        message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed.")
    phonenumber = models.CharField(validators=[phone_validator], max_length=10, unique=True, null= False, blank=False)
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} account is created successfully"