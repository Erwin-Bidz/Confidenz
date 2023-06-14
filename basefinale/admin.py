from django.contrib import admin
from basefinale.models import Entreprise, Fichier

# Register your models here.

@admin.register(Entreprise, Fichier)
class GenericAdmin(admin.ModelAdmin):
    pass