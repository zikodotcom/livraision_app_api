from django.db import models
from parcel.models import Parcel
import uuid
# Create your models here.

class DeleveryDocument(models.Model):
    id_delevery_doc = models.UUIDField(primary_key=True, default=uuid.uuid4)
    parcel = models.ManyToManyField(Parcel, related_name='delevery_parcel')