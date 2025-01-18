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
│   ├── controllers/
│   │   ├── login_controller.py
│   │   └── register_controller.py
│   ├── main_client.py
│   ├── utils/
│   │   └── protocole.py
│   └── vues/
│       ├── bienvenue_vue.py
│       ├── dashboard_vue.py
│       ├── login_vue.py
│       └── register_vue.py
├── server/
│   ├── controllers/
│   │   ├── trajet_controller.py
│   │   ��── user_controller.py
│   └── utils/
│       └── protocole.py
└── cov_application/
    └── modele/
        ├── utilisateur.py
        └── validation.py
```
