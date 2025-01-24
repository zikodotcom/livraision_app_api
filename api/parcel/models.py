from django.db import models
import uuid
from user.models import User
from zone.models import Zone

# Create your models here.


class Parcel(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='parcel_user')
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, related_name='parcel_zone')