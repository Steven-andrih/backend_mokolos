from django.db import models
from baseModels.models import BaseModel
from users.models import User
from holydays.models import Holyday
from permissions.models import Permission
# Create your models here.

class Comment(BaseModel):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    holyday = models.ForeignKey(Holyday, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

    def __str__(self) :
        return f'Auteur : {self.user.email}, Contenue : {self.content}, Permission : {self.permission}, Conge : {self.holyday}, ({self.id}) '

