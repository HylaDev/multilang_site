## Pré-requis
    - Django
    - Python
## Installation des dépendances
```sh
pip install -r requirements.txt
```

## Connexion à la base de données
    La base de données utilisée dans ce projet est PostgreSQL version 16.
    Elle est hébergée sur render.com, tout comme le projet.
    Avant de lancer le serveur, créez un fichier nommé .env, copiez et collez-y ce qui suit: DATABASE_URL = "postgres://doscod:c3kPxXh3dpnP7T3H42iONbcI8tfiNqyC@dpg-cpmnenlds78s73ak8ga0-a.oregon-postgres.render.com/blogdb_bds5"

## Création d'un superuser 
```sh
python manage.py createsuperuser
```
    
    puis suivez les instructions pour créer le superutilisateur.
    Un superutilisateur avec les informations d'identification suivantes a été créé : nom d'utilisateur=doscod et mot de passe=doscod
    
## Lancer le server
    python manage.py runserver

## Espace admin
    http://127.0.0.1:8000/admin/

## Traduction des éléments statiques
    rosetta a été utilisée pour faciliter la traduction de mots et de phrases statiques. Allez sur http://127.0.0.1:8000/rosetta/ pour accéder à son espace d'administration.
