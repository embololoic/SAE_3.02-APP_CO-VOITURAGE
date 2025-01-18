import unittest
from unittest.mock import MagicMock, patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'server')))
from server.controllers.trajet_controller import add_trajet, list_trajets, search_trajets, delete_trajet

class TestTrajetController(unittest.TestCase):

    @patch('server.controllers.trajet_controller.TrajetModel')
    def test_add_trajet(self, MockTrajetModel):
        mock_trajet_model = MockTrajetModel.return_value
        mock_trajet_model.create_trajet.return_value = 1

        data = {
            "conducteur_id": 2,
            "depart": "Paris",
            "arrivee": "Lyon",
            "date_heure": "2025-01-16 10:00:00",
            "prix": 30.0,
            "places_disponibles": 4
        }
        response = add_trajet(data)
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["trajet_id"], 1)

    @patch('server.controllers.trajet_controller.TrajetModel')
    def test_list_trajets(self, MockTrajetModel):
        mock_trajet_model = MockTrajetModel.return_value
        mock_trajet_model.get_all_trajets.return_value = [
            {"id": 1, "depart": "Paris", "arrivee": "Lyon"}
        ]

        response = list_trajets()
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["trajets"]), 1)
        self.assertEqual(response["trajets"][0]["depart"], "Paris")

    @patch('server.controllers.trajet_controller.TrajetModel')
    def test_search_trajets(self, MockTrajetModel):
        mock_trajet_model = MockTrajetModel.return_value
        mock_trajet_model.search_trajets.return_value = [
            {"id": 1, "depart": "Marseille", "arrivee": "Nice"}
        ]

        filters = {"depart": "Marseille", "arrivee": "Nice"}
        response = search_trajets(filters)
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["trajets"]), 1)
        self.assertEqual(response["trajets"][0]["depart"], "Marseille")

    @patch('server.controllers.trajet_controller.TrajetModel')
    def test_delete_trajet(self, MockTrajetModel):
        mock_trajet_model = MockTrajetModel.return_value
        mock_trajet_model.delete_trajet.return_value = True

        response = delete_trajet(1)
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["message"], "Trajet supprimé avec succès.")

if __name__ == "__main__":
    unittest.main()