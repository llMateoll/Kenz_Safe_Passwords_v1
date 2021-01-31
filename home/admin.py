from django.contrib import admin
from .models import Clave

# Register your models here.
@admin.register(Clave)
class ClaveAdmin(admin.ModelAdmin):
    list_display = ("url", "email", "username", "passwordtwo", "created_at", "updated_at")