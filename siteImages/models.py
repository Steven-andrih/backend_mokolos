from django.db import models

from baseModels.models import BaseModel

class SiteImage(BaseModel):
    file = models.CharField(max_length=255) # Chemin ou nom / fichier image

    def __str__(self):
        return self.file
