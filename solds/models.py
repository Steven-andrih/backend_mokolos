from django.db import models
from baseModels.models import BaseModel
from users.models import User
from datetime import date
# Create your models here.

class Sold(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solds')
    year = models.CharField(default= str(date.today().year))
    sold = models.IntegerField(default= 30)

    def __str__(self) :
        return f'Sold : N° :{self.id}, year : {self.year}, sold : {self.sold}'