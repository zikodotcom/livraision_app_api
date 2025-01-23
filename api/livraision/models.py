from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    choices = ['admin', 'client', 'livreur']
    email_verefied_at = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=10)
    type = models.Choices(value=choices)
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

# class Zone(models.Model):

class Colis(models.Model):
    id_colis = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    merchandise = models.CharField(max_length=255)
    quantity = models.IntegerField()
    adresse = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    is_replaced = models.BooleanField()
    is_openable = models.BooleanField()
    is_fragile = models.BooleanField()


