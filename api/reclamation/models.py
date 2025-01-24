from django.db import models
import uuid
from user.models import User
# Create your models here.

class Reclamation(models.Model):
    id_reclamation = models.UUIDField(primary_key=True, default=uuid.uuid4)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reclamation_user')