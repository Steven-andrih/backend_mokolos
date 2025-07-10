
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .models import UserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='employer', **extra_fields):
        if not email:
            raise ValueError("L'email est requis.")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, role='admin', is_staff=True, is_superuser=True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('rh', 'Rh'),
        ('employer', 'Employer'),

    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # nécessaire pour admin

    image = models.CharField(max_length=255, null=True)
    roles = models.TextField()
    position = models.CharField(max_length=255)
    description = models.TextField(null=True)
    last_change_request = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'  # login par email
    REQUIRED_FIELDS = []

    objects: 'UserManager' = UserManager()

    def __str__(self):
        return self.email

