## Installation des dépendances
    pip install -r requirements.txt

## Connexion à la base de données
    La base de données utilisée dans ce projet est PostgreSQL version 16.
    Elle est hébergée sur render.com, tout comme le projet.
    Avant de lancer le serveur, créez un fichier nommé .env, copiez et collez-y ce qui suit: DATABASE_URL = "postgres://doscod:c3kPxXh3dpnP7T3H42iONbcI8tfiNqyC@dpg-cpmnenlds78s73ak8ga0-a.oregon-postgres.render.com/blogdb_bds5"

## Création d'un superuser 
    python manage.py createsuperuser
    
## Lancer le server
    python manage.py runserver
