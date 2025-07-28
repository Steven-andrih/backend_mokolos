from django.db import models
from baseModels.models import BaseModel
from users.models import User
from django.utils import timezone
class Holyday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holydays')
    request_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_reasons = models.CharField(max_length=255)
    total = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'En attente'), ('approved', 'Approuvé'), ('rejected', 'Rejeté')],
        default='pending'
    )
    locale = models.CharField(max_length=10, default='fr')

    def __str__(self) :
        return f"Conge demande le {self.request_date}, du {self.start_date} au {self.end_date}, total: {self.total} Jours"

        # def save(self, *args, **kwargs):
        #     if self.start_date and self.end_date:
        #         self.total = (self.end_date - self.start_date).days + 1
        #     super().save(*args, **kwargs)

class CalculateHolyday(models.Model):
    weekendOption = models.BooleanField(null=True   )
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"Début de congé le {self.startDate} ,fin {self.endDate} , weekend : {self.weekendOption}"