from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('livreur', 'Livreur'),
    ]
    email_verefied_at = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=10)
    models.CharField(max_length=10, choices=ROLE_CHOICES)
    cin = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    adresse = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_type = models.CharField(max_length=10)
    cin_recto_image = models.ImageField(upload_to='image', blank=True, null=True)
    cin_verso_image = models.ImageField(upload_to='image', blank=True, null=True)
    rib_image = models.ImageField(upload_to='image', blank=True, null=True)
    bank_name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=255)
    bank_rib = models.CharField(max_length=255)
    dilevery_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

