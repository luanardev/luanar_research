from django.db import models
from django.db.models import DO_NOTHING
from datetime import datetime
import uuid
from account.models import User

# Create your models here.

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
