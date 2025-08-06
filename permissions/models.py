from django.db import models
from users.models import User
from baseModels.models import BaseModel

# Create your models here.
# class Permission(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, related_name="permissions")
#     start_date = models.DateField(auto_now_add=True)
#     end_date = models.DateField(auto_now_add=True)
#     beginning_hour = models.TimeField(auto_now_add=True)
#     end_time = models.TimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Permission de User : {self.user} , {self.start_date} au {self.end_date}"
    
# class PermissionTranslation(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#         ('cancelled', 'Cancelled'),
#     ]

#     permission = models.ForeignKey(Permission, on_delete=models.RESTRICT, related_name="permissions_translations")
#     nature_permission = models.CharField(max_length=255, null=True)
#     status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
#     locale = models.CharField(max_length=255, default='fr')

#     def __str__(self):
#         return f"Permission translation : {self.permission}, Nature : {self.nature_permission}"

class Permission(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="permissions")
    request_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()  # On laisse l’utilisateur choisir
    end_date = models.DateField()
    beginning_hour = models.DateTimeField()
    end_time = models.DateTimeField()
    nature = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'En attente'), ('approved', 'Approuvé'), ('rejected', 'Rejeté')],
        default='pending'
    )
    locale = models.CharField(max_length=10, default='fr')  

    def __str__(self):
        return f"{self.user} — Permission {self.nature} du {self.start_date} au {self.end_date} ,id : {self.id}"
