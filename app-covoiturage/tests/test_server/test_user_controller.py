#fichier de test  test_user_controller.py est  fonctionnel
import sys
import os
import unittest
from unittest.mock import MagicMock
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'server')))

from server.controllers.user_controller import UserController
from server.models.user import UserModel


class TestUserController(unittest.TestCase):
    def setUp(self):
        """
        Configure une instance de UserController avec une connexion simulée.
        """
        # Simule une connexion pour UserController
        mock_connection = MagicMock()
        self.user_controller = UserController(mock_connection)
        self.user_controller.utilisateur_model = MagicMock(spec=UserModel)

    def test_register_user_success(self):
        """
        Teste l'inscription réussie d'un utilisateur.
        """
        data = {
            "nom": "TestNom",
            "prenom": "TestPrenom",
            "email": "test@example.com",
            "mot_de_passe": "password123"
        }
        self.user_controller.utilisateur_model.create_user.return_value = 1
        response = self.user_controller.register_user(data)
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["message"], "Utilisateur créé avec succès.")
        self.assertEqual(response["user_id"], 1)

    def test_register_user_missing_field(self):
        """
        Teste l'échec de l'inscription lorsqu'un champ est manquant.
        """
        data = {
            "nom": "TestNom",
            "prenom": "TestPrenom",
            "email": "test@example.com"
        }
        response = self.user_controller.register_user(data)
        self.assertEqual(response["status"], "error")
        self.assertIn("Le champ mot_de_passe est requis.", response["message"])

    def test_login_user_success(self):
        """
        Teste la connexion réussie d'un utilisateur.
        """
        data = {
            "email": "test@example.com",
            "mot_de_passe": "password123"
        }
        self.user_controller.utilisateur_model.get_user_by_email.return_value = {
            "nom": "TestNom",
            "prenom": "TestPrenom",
            "email": "test@example.com",
            "mot_de_passe": "password123"
        }
        response = self.user_controller.login_user(data)
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["message"], "Connexion réussie.")

    def test_login_user_wrong_password(self):
        """
        Teste l'échec de la connexion avec un mot de passe incorrect.
        """
        data = {
            "email": "test@example.com",
            "mot_de_passe": "wrongpassword"
        }
        self.user_controller.utilisateur_model.get_user_by_email.return_value = {
            "nom": "TestNom",
            "prenom": "TestPrenom",
            "email": "test@example.com",
            "mot_de_passe": "password123"
        }
        response = self.user_controller.login_user(data)
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Mot de passe incorrect.")

    def test_get_user_success(self):
        """
        Teste la récupération des détails d'un utilisateur existant.
        """
        self.user_controller.utilisateur_model.get_user_by_id.return_value = {
            "nom": "TestNom",
            "prenom": "TestPrenom",
            "email": "test@example.com"
        }
        response = self.user_controller.get_user(1)
        self.assertEqual(response["status"], "success")
        self.assertIn("user", response)

    def test_get_user_not_found(self):
        """
        Teste la récupération d'un utilisateur qui n'existe pas.
        """
        self.user_controller.utilisateur_model.get_user_by_id.return_value = None
        response = self.user_controller.get_user(1)
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Utilisateur introuvable.")


if __name__ == "__main__":
    unittest.main()
