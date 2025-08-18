from django.db import models
from baseModels.models import BaseModel
# Create your models here.
class Faq(BaseModel):
    pass
    def __str__(self):
        return f"Faq : {self.id}"
class FaqTranslation(BaseModel):
    translatable = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name="translations")
    question = models.CharField(max_length=255)
    answer = models.TextField()
    locale = models.CharField(max_length=255)