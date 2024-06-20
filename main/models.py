"""Importation des modules nécessaires"""
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Posts(TranslatableModel):
    """
    Table "Posts" pour enregistrer les publications

    Attributes:
        title (CharField): Le titre de la publication
        content (TextField): Contenu de la publication
        publication_date (Date): Date de la publication

    Methods:
        __str__: Retourne le titre de la publication sur l'espace admin
    """
    translations = TranslatedFields(
        title=models.CharField(max_length=50),
        content=models.TextField(),
        )
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title   # pylint: disable=maybe-no-member
