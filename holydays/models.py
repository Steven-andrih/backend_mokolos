from django.db import models
from baseModels.models import BaseModel
from users.models import User

# Create your models here.
class Holyday(BaseModel):
    request_date = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    total = models.IntegerField(null=True)

    def __str__(self) :
        return f"Congé du {self.start_date} au {self.end_date} , Envoyer le {self.request_date}"

class HolydayTranslation(models.Model):
    translatable = models.ForeignKey(Holyday, on_delete=models.RESTRICT)
    leave_reasons = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    locale = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Translation du "

class HolydayUser(models.Model):
    holyday = models.ForeignKey(Holyday, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)