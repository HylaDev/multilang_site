"""Importation des modules nécessaires"""
from django.contrib import admin
from .models import Posts


admin.site.register(Posts)
