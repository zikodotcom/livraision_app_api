from django.db import models
import uuid
from user.models import User
# Create your models here.

class Personalised_price(models.Model):
    id_personalised_price = models.UUIDField(primary_key=True, default=uuid.uuid4)
    new_price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personalised_price_user')