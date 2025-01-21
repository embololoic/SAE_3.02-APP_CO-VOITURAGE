import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
import logging
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox
from client.utils.protocole import send_request

# Configurer le logging
logging.basicConfig(level=logging.INFO)

class TrajetController(QObject):
    """
    Contrôleur pour gérer les actions liées aux trajets.
    """
    def __init__(self, ajouter_trajet_view, voir_trajets_view):
        super().__init__()
        self.ajouter_trajet_view = ajouter_trajet_view
        self.voir_trajets_view = voir_trajets_view

        # Connexion des boutons
        self.ajouter_trajet_view.add_button.clicked.connect(self.ajouter_trajet)

    def calculer_impact_carbone(self, distance_km, facteur_emission=150, passagers=1):
        """
        Calcule l'impact carbone total et par personne.

        :param distance_km: Distance en kilomètres (float).
        :param facteur_emission: Facteur d'émission en gCO₂/km (par défaut 150 gCO₂/km).
        :param passagers: Nombre de passagers dans le véhicule (int, par défaut 1).
        :return: Impact carbone total en gCO₂ (float).
        """
        if passagers <= 0:
            raise ValueError("Le nombre de passagers doit être supérieur à 0.")

        impact_total = distance_km * facteur_emission
        return impact_total

    def ajouter_trajet(self):
        """
        Ajoute un nouveau trajet en envoyant une requête au serveur.
        """
        try:
            # Conversion des champs texte en valeurs numériques
            distance_km = float(self.ajouter_trajet_view.distance_input.text())
            passagers = int(self.ajouter_trajet_view.places_input.text())
            impact_carbone = self.calculer_impact_carbone(distance_km, passagers=passagers)

            trajet_data = {
                "conducteur_id": int(self.ajouter_trajet_view.conducteur_id_input.text()),
                "depart": self.ajouter_trajet_view.depart_input.text(),
                "arrivee": self.ajouter_trajet_view.destination_input.text(),
                "date_heure": self.ajouter_trajet_view.date_input.text(),
                "prix": float(self.ajouter_trajet_view.prix_input.text()),
                "places_disponibles": passagers,
                "distance_km": distance_km,
                "impact_carbone": impact_carbone,
                "cout_total": float(self.ajouter_trajet_view.cout_total_input.text()),
                "description": self.ajouter_trajet_view.description_input.toPlainText(),
            }

            logging.info(f"[LOG] Tentative d'ajout du trajet : {trajet_data}")
            response = send_request("add_trajet", trajet_data)

            if response and response.get("status") == "success":
                logging.info("[LOG] Trajet ajouté avec succès.")
                QMessageBox.information(self.ajouter_trajet_view, "Succès", "Trajet ajouté avec succès!")
            else:
                error_message = response.get("message", "Erreur lors de l'ajout du trajet.")
                logging.error(f"[LOG] Erreur : {error_message}")
                QMessageBox.critical(self.ajouter_trajet_view, "Erreur", error_message)
        except ValueError as ve:
            logging.error(f"[LOG] Erreur de conversion des données : {ve}")
            QMessageBox.critical(self.ajouter_trajet_view, "Erreur", "Veuillez entrer des valeurs valides.")
        except Exception as e:
            logging.error(f"[LOG] Erreur inattendue : {e}")
            QMessageBox.critical(self.ajouter_trajet_view, "Erreur", "Une erreur inattendue s'est produite.")
