from django.db import models
from personalised_price.models import Personalised_price
from user.models import User
from zone.models import Zone
import uuid
# Create your models here.

class City(models.Model):
    id_city = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    Personalised_price = models.ForeignKey(Personalised_price, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='city_user')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,related_name='city_zone')