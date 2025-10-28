from django.contrib import admin
from .models import Pokemon, Trainer

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']  # ← Solo name y type que SÍ existen
    search_fields = ['name', 'type']

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastName']  # ← Solo name y lastName
    search_fields = ['name', 'lastName']