# SAE_3.02-APP_CO-VOITURAGE
application graphique PyQt client/serveur de co-voiturage

# Application de Co-voiturage

## Description
Une application graphique client/serveur de co-voiturage développée en Python avec PyQt, permettant aux utilisateurs de partager des trajets entre leur domicile et leur lieu de travail.

## Fonctionnalités
- Inscription et gestion de compte utilisateur
- Importation d'emplois du temps au format iCalendar
- Recherche de covoiturages compatibles
- Sélection et confirmation des trajets
- Calcul et affichage des statistiques (coûts, distances, bilan carbone)

## Installation
1. Clonez le dépôt 
2. Installez les dépendances

## Arborecence de l'application de Co-voiturage
```
App-Covoiturage/
├── client/
│   ├── __init__.py
│   ├── main_client.py          # Point d'entrée pour l'application cliente
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── login_controller.py # Contrôleur pour la connexion
│   │   ├── register_controller.py # Contrôleur pour l'inscription
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── protocole.py        # Protocole pour envoyer des requêtes au serveur
│   │   ├── example.ics         # Exemple de fichier iCalendar
│   ├── vues/
│   │   ├── __init__.py
│   │   ├── bienvenue_vue.py    # Vue pour la page de bienvenue
│   │   ├── login_vue.py        # Vue pour la page de connexion
│   │   ├── register_vue.py     # Vue pour la page d'inscription
│   │   ├── dashboard_vue.py    # Vue pour le tableau de bord
├── server/
│   ├── __init__.py
│   ├── main_server.py          # Point d'entrée pour le serveur
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── protocole.py        # Protocole pour gérer les connexions client
│   │   ├── database.sql        # Script de création de la base de données
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── trajet_controller.py # Contrôleur pour les trajets
│   │   ├── user_controller.py  # Contrôleur pour les utilisateurs
│   ├── models/
│   │   ├── __init__.py
│   │   ├── trajet.py           # Modèle pour les trajets
│   │   ├── user.py             # Modèle pour les utilisateurs
├── tests/
│   ├── __init__.py
│   ├── test_client.py          # Tests pour les fonctionnalités du client
│   ├── test_server.py          # Tests pour les fonctionnalités du serveur
│   ├── test_protocole.py       # Tests pour le protocole de communication
├── requirements.txt            # Liste des dépendances Python (PyQt5, MySQLdb, etc.)
├── README.md                   # Documentation générale du projet

```
