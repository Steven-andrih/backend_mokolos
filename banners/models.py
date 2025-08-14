from django.db import models
from baseModels.models import BaseModel
from siteImages.models import SiteImage
# Create your models here.
class Banner(BaseModel):
    auto_play = models.BooleanField(default=False)
    animation = models.CharField(max_length=255)
    indicators = models.BooleanField(default=False)
    timeout = models.IntegerField()
    nav_buttons_always_visible = models.BooleanField(default=False)
    cycle_navigation = models.BooleanField(default=False)
    index_banner = models.IntegerField()

class BannerItem(BaseModel):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name="items")
    image = models.ForeignKey(SiteImage, on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.IntegerField()
    duration = models.FloatField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)