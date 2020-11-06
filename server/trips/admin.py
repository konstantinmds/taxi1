from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
  pass
