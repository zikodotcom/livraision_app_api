from django.db import models
import uuid
from parcel.models import Parcel
# Create your models here.

class PickUp(models.Model):
    id_pickup = models.UUIDField(primary_key=True, default=uuid.uuid4)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE,related_name='pickup_parcel')