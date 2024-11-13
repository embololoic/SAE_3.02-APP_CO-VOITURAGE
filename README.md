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
cov-application/
│
├── client/
│   ├── controllers/       # Gère la logique des actions utilisateur
│   ├── models/            # Modèle - Gestion des données et règles métier
│   ├── views/             # Vue - Interfaces graphiques en PyQt
│   ├── utils/             # Fonctions utilitaires
│   ├── app_covoiturage-client.py            # Point d'entrée du client
│
├── server/
│   ├── controllers/       # Gère les requêtes clients et l'authentification
│   ├── models/            # Modèle - Gestion des données serveur
│   ├── app_covoiturage-server.py            # Point d'entrée du serveur
│
├── database/
│   ├── schema.sql         # Schéma de la base de données
│   ├── initialize.py      # Script d'initialisation de la base de données
│
├── tests/                 # Répertoire pour les tests unitaires
│
├── docs/                  # Documentation du projet
│
├── README.rst             # Description du projet
├── requirements.txt       # Dépendances du projet
└── .git/                  # Dépôt Git pour le versionnement
```
