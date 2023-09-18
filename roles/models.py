from django.db import models


# Create your models here.
class Roles(models.Model):
    DoesNotExist = None
    objects = None
    libelle = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.libelle
