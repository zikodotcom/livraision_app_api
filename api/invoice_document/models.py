from django.db import models
import uuid
from parcel.models import Parcel
# Create your models here.
class InvoiceDocument(models.Model):
    id_invoice_doc = models.UUIDField(primary_key=True, default=uuid.uuid4)
    parcel = models.ManyToManyField(Parcel, related_name='invoice_parcel')