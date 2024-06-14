"""Importation des modules nécessaires"""
from django.contrib import admin
from .models import Posts
from parler.admin import TranslatableAdmin


admin.site.register(Posts, TranslatableAdmin)
