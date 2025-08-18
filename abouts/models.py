from django.db import models
from baseModels.models import BaseModel
from siteImages.models import SiteImage
# Create your models here.
class About(BaseModel):
    image = models.ForeignKey(SiteImage, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"About : {self.id}"
class AboutTranslation(BaseModel):
    translatable = models.ForeignKey(About, on_delete=models.CASCADE, related_name="translations")
    title = models.CharField(max_length=255)
    description = models.TextField()
    locale = models.CharField(max_length=255)