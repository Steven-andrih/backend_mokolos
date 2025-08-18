from django.db import models
from baseModels.models import BaseModel
# Create your models here.
class Section(BaseModel):
    pass

    def __str__(self):
        return f"Section : {self.id}"

class SectionTranslation(BaseModel):
    translatable = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="translations")
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    locale = models.CharField(max_length=255)
