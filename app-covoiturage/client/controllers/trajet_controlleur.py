import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
import socket
import json
from PyQt5.QtCore import QObject, pyqtSlot
from client.models.trajet_model import TrajetModel

class TrajetController(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.view.submit_button.clicked.connect(self.add_trajet)

    @pyqtSlot()
    def add_trajet(self):
        """
        Handles the addition of a new trip.

        Collects the trip data from the view, creates a TrajetModel instance,
        and sends the data to the server.

        Parameters:
        None

        Returns:
        None
        """
        # Collect input data
        try:
            trajet = TrajetModel(
                depart=self.view.depart_input.text(),
                arrivee=self.view.arrivee_input.text(),
                date_heure=self.view.date_heure_input.text(),
                prix=float(self.view.prix_input.text()),
                places_disponibles=int(self.view.places_input.text())
            )
        except ValueError:
            self.view.show_error_message("Invalid input! Please check the fields.")
            return

        # Send data to the server
        try:
            response = self.send_to_server(trajet.to_json())
            if response.get("status") == "success":
                self.view.show_success_message()
            else:
                self.view.show_error_message(response.get("message", "Unknown error"))
        except Exception as e:
            self.view.show_error_message(str(e))

    