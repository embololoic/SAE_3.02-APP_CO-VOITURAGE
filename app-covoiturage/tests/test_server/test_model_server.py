#test fonctionnel du model du  serveur

import unittest
import MySQLdb
import sys
import os
from unittest.mock import MagicMock  # Ajout de l'importation de MagicMock
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'server')))
from server.models.user import UserModel
from server.models.trajet import TrajetModel
from server.controllers.user_controller import UserController  # Ajout de l'importation de UserController

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Initialisation de la connexion à la base de données pour les tests.
        """
        cls.conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="covoiturage")
        cls.user_model = UserModel(cls.conn)
        cls.trajet_model = TrajetModel(cls.conn)

    @classmethod
    def tearDownClass(cls):
        """
        Fermeture de la connexion à la base de données après les tests.
        """
        cls.conn.close()

    def setUp(self):
        """
        Réinitialisation des tables avant chaque test.
        """
        self.mock_conn = MagicMock()
        self.user_controller = UserController(self.mock_conn)
        self.user_controller.utilisateur_model = MagicMock(spec=UserModel)

        cursor = self.conn.cursor()
        # Réinitialise les tables
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        # Supprimer les données des tables
        cursor.execute("TRUNCATE TABLE reservations;")
        cursor.execute("TRUNCATE TABLE trajets;")
        cursor.execute("TRUNCATE TABLE utilisateurs;")
        # Rétablir les contraintes de clés étrangères
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        # Valider les modifications
        self.conn.commit()

    def test_create_user(self):
        """
        Test de la création d'un utilisateur.
        """
        user_data = {
            "nom": "TestNom",
            "prenom": "TestPrenom",
            "email": "test@example.com",
            "mot_de_passe": "password123"
        }
        user_id = self.user_model.create_user(user_data)
        self.assertIsNotNone(user_id)

        # Vérifie si l'utilisateur existe dans la base
        user = self.user_model.get_user_by_email("test@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user["nom"], "TestNom")
        self.assertEqual(user["prenom"], "TestPrenom")

    def test_create_trajet(self):
        """
        Test de la création d'un trajet.
        """
        # Crée un utilisateur pour être le conducteur
        user_data = {
            "nom": "Conducteur",
            "prenom": "Exemple",
            "email": "conducteur@example.com",
            "mot_de_passe": "securepassword"
        }
        conducteur_id = self.user_model.create_user(user_data)

        # Crée un trajet
        trajet_data = {
            "conducteur_id": conducteur_id,
            "depart": "Paris",
            "arrivee": "Lyon",
            "date_heure": "2025-01-15 10:00:00",
            "prix": 30.0,
            "places_disponibles": 4
        }
        trajet_id = self.trajet_model.create_trajet(trajet_data)
        self.assertIsNotNone(trajet_id)

        # Vérifie si le trajet existe dans la base
        trajets = self.trajet_model.get_all_trajets()
        self.assertEqual(len(trajets), 1)
        self.assertEqual(trajets[0]["depart"], "Paris")
        self.assertEqual(trajets[0]["arrivee"], "Lyon")

    def test_search_trajet(self):
        """
        Test de la recherche de trajets.
        """
        # Crée un utilisateur et un trajet
        user_data = {
            "nom": "Conducteur",
            "prenom": "Recherche",
            "email": "recherche@example.com",
            "mot_de_passe": "passwordsearch"
        }
        conducteur_id = self.user_model.create_user(user_data)

        trajet_data = {
            "conducteur_id": conducteur_id,
            "depart": "Marseille",
            "arrivee": "Nice",
            "date_heure": "2025-01-20 08:00:00",
            "prix": 25.0,
            "places_disponibles": 3
        }
        self.trajet_model.create_trajet(trajet_data)

        # Recherche un trajet
        filters = {"depart": "Marseille", "arrivee": "Nice"}
        result = self.trajet_model.search_trajets(filters)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["depart"], "Marseille")
        self.assertEqual(result[0]["arrivee"], "Nice")

if __name__ == "__main__":
    unittest.main()