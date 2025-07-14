from django.contrib import admin
from .models import Permission, PermissionTranslation

# Register your models here.
admin.site.register(Permission)
admin.site.register(PermissionTranslation)
