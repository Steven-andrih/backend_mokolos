from django.db import models
from baseModels.models import BaseModel
from users.models import User
from django.utils import timezone

# Create your models here.
# class Holyday(BaseModel):
#     request_date = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateField(default= timezone.now)
#     end_date = models.DateField(default= timezone.now)
#     total = models.IntegerField(null=True)

#     def __str__(self) :
#         return f"Congé du {self.start_date} au {self.end_date} , Envoyer le {self.request_date}"

# class HolydayTranslation(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#         ('cancelled', 'Cancelled'),
#     ]
#     translatable = models.ForeignKey(Holyday, on_delete=models.RESTRICT , related_name='holydayTranslations')
#     leave_reasons = models.CharField(max_length=255, null=True)
#     status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
#     locale = models.CharField(max_length=255, default='fr')

#     def __str__(self):
#         return f"Translation du {self.translatable}, status:{self.status}, locale:{self.locale}"

# class HolydayUser(models.Model):
#     holyday = models.ForeignKey(Holyday, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

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

    def save(self, *args, **kwargs):
        if self.start_date and self.end_date:
            self.total = (self.end_date - self.start_date).days + 1
        super().save(*args, **kwargs)
