"""Importation des modules nécessaires"""
from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Posts


admin.site.register(Posts, TranslatableAdmin)
