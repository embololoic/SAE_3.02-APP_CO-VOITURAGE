import logging
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from client.utils.protocole import send_request

class GererTrajetController(QObject):
    """
    Controller for managing trips.
    """
    def __init__(self, view):
        """
                Initializes the trip management controller.

                Args:
                    view: The view associated with trip management.
        """
        super().__init__()
        self.view = view

        # Connexion des boutons
        self.view.refresh_button.clicked.connect(self.actualiser_trajets)
        self.view.delete_button.clicked.connect(self.supprimer_trajet)

    def actualiser_trajets(self):
        """
        Retrieves the list of trips from the server.
        """
        logging.info("[LOG] Récupération des trajets...")
        response = send_request("list_trajets", {})
        if response and response.get("status") == "success":
            trajets = response.get("trajets", [])
            self.view.populate_table(trajets)
            logging.info("[LOG] Trajets récupérés avec succès.")
        else:
            error_message = response.get("message", "Erreur lors de la récupération des trajets.")
            logging.error(f"[LOG] {error_message}")
            QMessageBox.critical(self.view, "Erreur", error_message)

    def supprimer_trajet(self):
        """
        Deletes the selected trip.
        """
        trajet_id = self.view.get_selected_trajet_id()
        if not trajet_id:
            QMessageBox.warning(self.view, "Avertissement", "Veuillez sélectionner un trajet à supprimer.")
            return

        logging.info(f"[LOG] Suppression du trajet ID {trajet_id}...")
        response = send_request("delete_trajet", {"trajet_id": trajet_id})
        if response and response.get("status") == "success":
            QMessageBox.information(self.view, "Succès", "Trajet supprimé avec succès!")
            self.actualiser_trajets()  # Actualiser la table après suppression
        else:
            error_message = response.get("message", "Erreur lors de la suppression du trajet.")
            logging.error(f"[LOG] {error_message}")
            QMessageBox.critical(self.view, "Erreur", error_message)
