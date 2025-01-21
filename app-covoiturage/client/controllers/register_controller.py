import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from client.utils.protocole import send_request


class RegisterController:
    def __init__(self, view, show_dashboard_callback):
        self.view = view
        self.is_processing = False
        self.show_dashboard_callback = show_dashboard_callback
        # Connexion sécurisée du signal
        if self.view.btn_inscription.receivers(self.view.btn_inscription.clicked) > 0:
            self.view.btn_inscription.clicked.disconnect()
        self.view.btn_inscription.clicked.connect(self.inscrire_utilisateur)

    def inscrire_utilisateur(self):
        if self.is_processing:
            print("Requête déjà en cours. Ignorée.")
            return

        print("Tentative d'inscription déclenchée - Début")
        self.is_processing = True
        self.view.btn_inscription.setEnabled(False)

        try:
            data = {
                "nom": self.view.input_nom.text(),
                "prenom": self.view.input_prenom.text(),
                "email": self.view.input_email.text(),
                "mot_de_passe": self.view.input_password.text(),
                "adresse": self.view.input_adresse.text(),
                "coordonnees_gps": self.view.input_gps.text(),
                "places_voiture": self.view.input_places.value(),
                "cv_fiscaux": self.view.input_cv.value(),
                "indisponibilites": self.get_indisponibilite(),
                "emploi_du_temps": self.view.label_calendar.text()
            }

            print("Données collectées :", data)

            if self.validate_data(data):
                print("Validation des données réussie")
                response = send_request("register", data)

                print("Réponse reçue :", response)
                if response:
                    if response.get("status") == "success":
                        user_id = response.get("user_id")  # Récupérer l'ID utilisateur
                        print(f"Inscription réussie avec l'ID utilisateur : {user_id}")
                        QMessageBox.information(
                            self.view,
                            "Succès",
                            f"Inscription réussie! Votre ID utilisateur est : {user_id}"
                        )
                        self.reset_form()
                        self.view.btn_inscription.setEnabled(True)  # Réactiver le bouton après succès
                        self.show_dashboard_callback()
                    elif response.get("message") == "Cet email est déjà utilisé.":
                        print("Erreur : Email déjà utilisé")
                        QMessageBox.critical(self.view, "Erreur", "Cet email est déjà utilisé. Veuillez en choisir un autre.")
                    else:
                        print("Erreur inconnue :", response.get("message", "Erreur inconnue"))
                        QMessageBox.critical(self.view, "Erreur", response.get("message", "Erreur inconnue."))
                else:
                    print("Erreur : Pas de réponse du serveur")
                    QMessageBox.critical(self.view, "Erreur", "Erreur lors de la communication avec le serveur.")
            else:
                print("Validation échouée : Champs obligatoires manquants")
                QMessageBox.critical(self.view, "Erreur", "Veuillez remplir tous les champs obligatoires.")
        except Exception as e:
            print("Erreur inattendue :", e)
        finally:
            print("Fin du traitement d'inscription")
            self.is_processing = False
            self.view.btn_inscription.setEnabled(True)

    def validate_data(self, data):
        required_fields = ["nom", "prenom", "email", "mot_de_passe"]
        for field in required_fields:
            if not data[field]:
                print(f"Champ manquant : {field}")
                return False
        return True

    def get_indisponibilite(self):
        jours = []
        if self.view.check_lundi.isChecked():
            jours.append("Lundi")
        if self.view.check_mardi.isChecked():
            jours.append("Mardi")
        if self.view.check_mercredi.isChecked():
            jours.append("Mercredi")
        if self.view.check_jeudi.isChecked():
            jours.append("Jeudi")
        if self.view.check_vendredi.isChecked():
            jours.append("Vendredi")
        if self.view.check_samedi.isChecked():
            jours.append("Samedi")
        if self.view.check_dimanche.isChecked():
            jours.append("Dimanche")
        return ", ".join(jours)

    def reset_form(self):
        print("Réinitialisation du formulaire")
        self.view.input_nom.clear()
        self.view.input_prenom.clear()
        self.view.input_email.clear()
        self.view.input_password.clear()
        self.view.input_adresse.clear()
        self.view.input_gps.clear()
        self.view.input_places.setValue(1)
        self.view.input_cv.setValue(1)
        self.view.check_lundi.setChecked(False)
        self.view.check_mardi.setChecked(False)
        self.view.check_mercredi.setChecked(False)
        self.view.check_jeudi.setChecked(False)
        self.view.check_vendredi.setChecked(False)
        self.view.check_samedi.setChecked(False)
        self.view.check_dimanche.setChecked(False)
        self.view.label_calendar.setText("Emploi du temps (iCalendar) :")
