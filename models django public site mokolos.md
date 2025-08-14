# models.py

from django.db import models
from baseModels.models import BaseModel

class Image(BaseModel):
"""Table qui stocke toutes les images."""
file = models.CharField(max_length=255) # Chemin ou nom du fichier image

    def __str__(self):
        return self.file

class About(BaseModel):
image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)

class AboutTranslation(BaseModel):
translatable = models.ForeignKey(About, on_delete=models.CASCADE, related_name="translations")
title = models.CharField(max_length=255)
description = models.TextField()
locale = models.CharField(max_length=255)

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
image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
order_number = models.IntegerField()
duration = models.FloatField()
title = models.CharField(max_length=255)
description = models.CharField(max_length=255)

class Service(BaseModel):
pass

class ServiceTranslation(BaseModel):
translatable = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="translations")
title = models.CharField(max_length=255)
sub_title = models.TextField()
locale = models.CharField(max_length=255)

class Section(BaseModel):
pass

class SectionTranslation(BaseModel):
translatable = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="translations")
title = models.CharField(max_length=255)
sub_title = models.CharField(max_length=255)
locale = models.CharField(max_length=255)

class Faq(BaseModel):
pass

class FaqTranslation(BaseModel):
translatable = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name="translations")
question = models.CharField(max_length=255)
answer = models.TextField()
locale = models.CharField(max_length=255)

class Technology(BaseModel):
name = models.CharField(max_length=255)
image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)

class Contact(BaseModel):
full_name = models.CharField(max_length=255)
email = models.CharField(max_length=255)
phone_number = models.CharField(max_length=255)
subject = models.TextField()
message = models.TextField()

// Admin.py
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
SiteImage, About, AboutTranslation,
Banner, BannerItem,
Service, ServiceTranslation,
Section, SectionTranslation,
Faq, FaqTranslation,
Technology, Contact
)

# ==== IMAGE ====

@admin.register(SiteImage)
class SiteImageAdmin(ModelAdmin):
list_display = ("id", "file", "created_at", "updated_at")
search_fields = ("file",)
list_filter = ("created_at",)
ordering = ("-created_at",)

# ==== ABOUT ====

@admin.register(About)
class AboutAdmin(ModelAdmin):
list_display = ("id", "image", "created_at", "updated_at")
list_filter = ("created_at",)
search_fields = ("id",)
ordering = ("-created_at",)

@admin.register(AboutTranslation)
class AboutTranslationAdmin(ModelAdmin):
list_display = ("id", "translatable", "title", "locale")
list_filter = ("locale",)
search_fields = ("title", "description", "locale")

# ==== BANNER ====

@admin.register(Banner)
class BannerAdmin(ModelAdmin):
list_display = ("id", "auto_play", "animation", "timeout", "index_banner", "created_at")
list_filter = ("auto_play", "indicators", "cycle_navigation")
search_fields = ("animation",)
ordering = ("-created_at",)

@admin.register(BannerItem)
class BannerItemAdmin(ModelAdmin):
list_display = ("id", "banner", "order_number", "title", "duration")
list_filter = ("banner",)
search_fields = ("title", "description")

# ==== SERVICE ====

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
list_display = ("id", "created_at", "updated_at")
ordering = ("-created_at",)

@admin.register(ServiceTranslation)
class ServiceTranslationAdmin(ModelAdmin):
list_display = ("id", "translatable", "title", "locale")
list_filter = ("locale",)
search_fields = ("title", "sub_title")

# ==== SECTION ====

@admin.register(Section)
class SectionAdmin(ModelAdmin):
list_display = ("id", "created_at", "updated_at")

@admin.register(SectionTranslation)
class SectionTranslationAdmin(ModelAdmin):
list_display = ("id", "translatable", "title", "locale")
list_filter = ("locale",)
search_fields = ("title", "sub_title")

# ==== FAQ ====

@admin.register(Faq)
class FaqAdmin(ModelAdmin):
list_display = ("id", "created_at", "updated_at")

@admin.register(FaqTranslation)
class FaqTranslationAdmin(ModelAdmin):
list_display = ("id", "translatable", "question", "locale")
list_filter = ("locale",)
search_fields = ("question", "answer")

# ==== TECHNOLOGY ====

@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
list_display = ("id", "name", "image", "created_at")
search_fields = ("name",)
ordering = ("-created_at",)

# ==== CONTACT ====

@admin.register(Contact)
class ContactAdmin(ModelAdmin):
list_display = ("id", "full_name", "email", "phone_number", "created_at")
search_fields = ("full_name", "email", "phone_number", "subject", "message")
list_filter = ("created_at",)
