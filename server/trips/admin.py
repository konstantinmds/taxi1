from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User, Trip

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
  pass

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
  fields = (
    'id', 'pick_up_address', 'drop_off_address', 'status',
     'created', 'updated',
    )
  list_display = (
    'id', 'pick_up_address', 'drop_off_address', 'status',
     'created', 'updated',
    )
  list_filter = (
    'status',
    )
  readonly_fields = (
    'id', 'created', 'updated',
    )