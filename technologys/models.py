from django.db import models
from siteImages.models import SiteImage
from baseModels.models import BaseModel
# Create your models here.
class Technology(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(SiteImage, on_delete=models.SET_NULL, null=True, blank=True)