from django.db import models
from baseModels.models import BaseModel

# Create your models here.
class Contact(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    subject = models.TextField()
    message = models.TextField()