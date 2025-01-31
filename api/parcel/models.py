from django.db import models
import uuid
from user.models import User
from city.models import City

# Create your models here.


class Parcel(models.Model):
    ETAT = (
        ('1', 'Payé'),
        ('2', 'Non Payé	'),
    )
    STATUS = (
        ('1', 'Nouveau Colis'),
        ('2', 'Attente De Ramassage'),
        ('3', 'Ramassé'),
        ('4', 'Expédié'),
        ('5', 'Reçu'),
        ('6', 'Mise en distribution'),
        ('7', 'In progress'),
        ('8', 'Livré'),
        ('9', 'Retourné'),
    )
    id_colis = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    merchandise = models.CharField(max_length=255)
    quantity = models.IntegerField()
    adresse = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    etat = models.CharField(choices=ETAT, default=ETAT[1][1], max_length=4)
    status = models.CharField(choices=STATUS, default=STATUS[1][1], max_length=4)
    comment = models.TextField(blank=True, null=True)
    is_replaced = models.BooleanField()
    is_openable = models.BooleanField()
    is_fragile = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='parcel_user')
    city = models.ForeignKey(City,on_delete=models.CASCADE, related_name='parcel_city')