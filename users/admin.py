# users/admin.py
from django.contrib import admin
from unfold.admin import ModelAdmin  # Import Unfold ModelAdmin
from .models import User

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("email", "first_name", "last_name", "role","position", "description", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name", "role")
