from django.db import models
from baseModels.models import BaseModel
# Create your models here.

class Service(BaseModel):
    pass
    def __str__(self):
        return f"Service : {self.id}"
class ServiceTranslation(BaseModel):
    translatable = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="translations")
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    locale = models.CharField(max_length=255)