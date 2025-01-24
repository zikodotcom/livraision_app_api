from django.db import models
import uuid
# Create your models here.

class Zone(models.Model):
    id_zone = models.UUIDField(primary_key=True, default=uuid.uuid4)
    zone_name = models.CharField(max_length=255)
    zone_status = models.BooleanField(default=True)