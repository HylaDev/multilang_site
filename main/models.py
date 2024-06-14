"""Importation des modules nécessaires"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Posts(TranslatableModel):
    """
    Table "Posts" pour enregistrer les publications

    Attributes:
        title (CharField): Le titre de la publication
        content (TextField): Contenu de la publication
        publication_date (Date): Date de la publication

    Methods:
        __str__: Retourne le nom de la saison sur l'espace admin
    """
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField(),
        )
    publication_date = models.DateTimeField()

    def __str__(self):
        return str(self.title)
