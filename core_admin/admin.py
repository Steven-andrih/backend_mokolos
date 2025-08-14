from django.contrib import admin
from unfold.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from abouts.models import About, AboutTranslation
from banners.models import Banner, BannerItem
from services.models import Service, ServiceTranslation
from sections.models import Section, SectionTranslation
from faqs.models import Faq, FaqTranslation
from technologys.models import Technology
from contacts.models import Contact
from siteImages.models import SiteImage

# ==== IMAGE ====
@admin.register(SiteImage)
class SiteImageAdmin(ModelAdmin):
    unfold = {"icon": "image", "section": "Médias"}
    list_display = ("id", "file", "created_at", "updated_at")
    search_fields = ("file",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

# ==== ABOUT ====
@admin.register(About)
class AboutAdmin(ModelAdmin):
    unfold = {"icon": "info", "section": "Contenu Vitrine"}
    list_display = ("id", "image", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("id",)
    ordering = ("-created_at",)
    search_fields = ("id",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(AboutTranslation)
class AboutTranslationAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "translate", "section": "Contenu Vitrine"}
    list_display = ("id", "translatable", "title", "locale")
    list_filter = ("locale",)
    search_fields = ("title", "description", "locale")
    autocomplete_fields = ("translatable",)

# ==== BANNER ====
@admin.register(Banner)
class BannerAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "slideshow", "section": "Contenu Vitrine"}
    list_display = ("id", "auto_play", "animation", "timeout", "index_banner", "created_at")
    list_filter = ("auto_play", "indicators", "cycle_navigation")
    search_fields = ("animation",)
    ordering = ("-created_at",)
    list_editable = ("auto_play", "timeout", "index_banner")
    readonly_fields = ("created_at", "updated_at")

@admin.register(BannerItem)
class BannerItemAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "image", "section": "Contenu Vitrine"}
    list_display = ("id", "banner", "order_number", "title", "duration")
    list_filter = ("banner",)
    search_fields = ("title", "description")
    list_editable = ("order_number", "duration")
    autocomplete_fields = ("banner",)
    readonly_fields = ("created_at", "updated_at")

# ==== SERVICE ====
@admin.register(Service)
class ServiceAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "build", "section": "Contenu Vitrine"}
    list_display = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)
    search_fields = ("id",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(ServiceTranslation)
class ServiceTranslationAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "translate", "section": "Contenu Vitrine"}
    list_display = ("id", "translatable", "title", "locale")
    list_filter = ("locale",)
    search_fields = ("title", "sub_title")
    autocomplete_fields = ("translatable",)

# ==== SECTION ====
@admin.register(Section)
class SectionAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "view_agenda", "section": "Contenu Vitrine"}
    list_display = ("id", "created_at", "updated_at")
    search_fields = ("id",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(SectionTranslation)
class SectionTranslationAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "translate", "section": "Contenu Vitrine"}
    list_display = ("id", "translatable", "title", "locale")
    list_filter = ("locale",)
    search_fields = ("title", "sub_title")
    autocomplete_fields = ("translatable",)

# ==== FAQ ====
@admin.register(Faq)
class FaqAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "help", "section": "Contenu Vitrine"}
    list_display = ("id", "created_at", "updated_at")
    search_fields = ("id",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(FaqTranslation)
class FaqTranslationAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "translate", "section": "Contenu Vitrine"}
    list_display = ("id", "translatable", "question", "locale")
    list_filter = ("locale",)
    search_fields = ("question", "answer")
    autocomplete_fields = ("translatable",)

# ==== TECHNOLOGY ====
@admin.register(Technology)
class TechnologyAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "memory", "section": "Contenu Vitrine"}
    list_display = ("id", "name", "image", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

# ==== CONTACT ====
@admin.register(Contact)
class ContactAdmin(SimpleHistoryAdmin,ModelAdmin):
    unfold = {"icon": "contact_mail", "section": "Formulaires"}
    list_display = ("id", "full_name", "email", "phone_number", "created_at")
    search_fields = ("full_name", "email", "phone_number", "subject", "message")
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")
