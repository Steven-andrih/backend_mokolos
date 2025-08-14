from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    history = HistoricalRecords(inherit=True)
    class Meta:
        abstract = True
