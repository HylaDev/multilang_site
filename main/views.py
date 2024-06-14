"""Importation des modules nécessaires"""
from django.shortcuts import render
from .models import Posts


def home(request):
    """
    Affiche la page d'accueil du blog

    Args:
        request: Requête entrante

    Context:
    """
    posts = Posts.objects.all()  # pylint: disable=maybe-no-member
    context = {
        "posts": posts,
    }
    return render(request, 'blog/accueil.html', context)
