from django.db import models

# Create your models here.

class Clave(models.Model):
    url = models.URLField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=50, null=True, blank=True)
    passwordtwo = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']