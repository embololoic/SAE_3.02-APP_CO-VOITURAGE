import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QSpinBox, QCheckBox, QHBoxLayout, QMessageBox
from client.controllers.register_controller import RegisterController
from client.utils.validation import Validation

class PageRegister(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = RegisterController()
        self.init_ui()
        self.parent = parent  # Référence au parent pour la gestion des pages

    def init_ui(self):
        self.setWindowTitle("Inscription - Application de Covoiturage")
        self.setGeometry(100, 100, 500, 800)

        # Layout principal
        layout = QVBoxLayout()

        # Champs obligatoires
        self.label_nom = QLabel("Nom :")
        layout.addWidget(self.label_nom)
        self.input_nom = QLineEdit()
        self.input_nom.setPlaceholderText("Entrez votre nom")
        layout.addWidget(self.input_nom)

        self.label_prenom = QLabel("Prénom :")
        layout.addWidget(self.label_prenom)
        self.input_prenom = QLineEdit()
        self.input_prenom.setPlaceholderText("Entrez votre prénom")
        layout.addWidget(self.input_prenom)

        self.label_email = QLabel("Email :")
        layout.addWidget(self.label_email)
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Entrez votre email")
        layout.addWidget(self.input_email)

        self.label_password = QLabel("Mot de passe :")
        layout.addWidget(self.label_password)
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Créez un mot de passe")
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)

        # Adresse
        self.label_adresse = QLabel("Adresse :")
        layout.addWidget(self.label_adresse)
        self.input_adresse = QLineEdit()
        self.input_adresse.setPlaceholderText("Entrez votre adresse")
        layout.addWidget(self.input_adresse)

        # Coordonnées GPS (facultatif)
        self.label_gps = QLabel("Coordonnées GPS (facultatif) :")
        layout.addWidget(self.label_gps)
        self.input_gps = QLineEdit()
        self.input_gps.setPlaceholderText("Entrez vos coordonnées GPS")
        layout.addWidget(self.input_gps)

        # Nombre de places
        self.label_places = QLabel("Nombre de places dans la voiture :")
        layout.addWidget(self.label_places)
        self.input_places = QSpinBox()
        self.input_places.setMinimum(1)
        self.input_places.setMaximum(9)
        layout.addWidget(self.input_places)

        # CV fiscaux
        self.label_cv = QLabel("CV fiscaux :")
        layout.addWidget(self.label_cv)
        self.input_cv = QSpinBox()
        self.input_cv.setMinimum(1)
        self.input_cv.setMaximum(20)
        layout.addWidget(self.input_cv)

        # Jours d'indisponibilité
        self.label_indisponibilite = QLabel("Jours d'indisponibilité :")
        layout.addWidget(self.label_indisponibilite)
        jours_layout = QHBoxLayout()
        self.check_lundi = QCheckBox("Lundi")
        self.check_mardi = QCheckBox("Mardi")
        self.check_mercredi = QCheckBox("Mercredi")
        self.check_jeudi = QCheckBox("Jeudi")
        self.check_vendredi = QCheckBox("Vendredi")
        self.check_samedi = QCheckBox("Samedi")
        self.check_dimanche = QCheckBox("Dimanche")
        jours_layout.addWidget(self.check_lundi)
        jours_layout.addWidget(self.check_mardi)
        jours_layout.addWidget(self.check_mercredi)
        jours_layout.addWidget(self.check_jeudi)
        jours_layout.addWidget(self.check_vendredi)
        jours_layout.addWidget(self.check_samedi)
        jours_layout.addWidget(self.check_dimanche)
        layout.addLayout(jours_layout)

        # Emploi du temps
        self.label_calendar = QLabel("Emploi du temps (iCalendar) :")
        layout.addWidget(self.label_calendar)
        self.btn_calendar = QPushButton("Choisir un fichier")
        self.btn_calendar.clicked.connect(self.choisir_fichier)
        layout.addWidget(self.btn_calendar)

        # Bouton d'inscription
        self.btn_inscription = QPushButton("S'inscrire")
        self.btn_inscription.clicked.connect(self.s_inscrire)
        layout.addWidget(self.btn_inscription)


        # Appliquer le layout
        self.setLayout(layout)

    def choisir_fichier(self):
        """Ouvre un sélecteur de fichier pour choisir un fichier iCalendar."""
        fichier, _ = QFileDialog.getOpenFileName(self, "Sélectionner un fichier iCalendar", "", "Fichiers iCalendar (*.ics)")
        if fichier:
            self.label_calendar.setText(f"Fichier sélectionné : {fichier}")

    def s_inscrire(self):
        """Collecte les données et les envoie au contrôleur."""
        print("Début de l'inscription...")
        data = {
            "nom": self.input_nom.text(),
            "prenom": self.input_prenom.text(),
            "email": self.input_email.text(),
            "mot_de_passe": self.input_password.text(),
            "adresse": self.input_adresse.text(),
            "gps": self.input_gps.text(),
            "places_voiture": self.input_places.value(),
            "cv_fiscaux": self.input_cv.value(),
            "indisponibilites": ",".join([check.text() for check in [
                self.check_lundi, self.check_mardi, self.check_mercredi, self.check_jeudi,
                self.check_vendredi, self.check_samedi, self.check_dimanche
            ] if check.isChecked()]),
            "emploi_du_temps": self.label_calendar.text().replace("Fichier sélectionné : ", "") or None
        }
        print(f"Données collectées : {data}")

        # Validation des champs
        valide, message = Validation.champs_remplis(**data)
        if not valide:
            print(f"Validation échouée : {message}")
            QMessageBox.warning(self, "Erreur", message)
            return

        # Envoi au contrôleur
        print("Envoi des données au contrôleur...")
        response = self.controller.enregistrer_utilisateur(data)
        print(f"Réponse du contrôleur : {response}")

        if response.get("status") == "success":
            QMessageBox.information(self, "Succès", "Inscription réussie !")
        else:
            QMessageBox.warning(self, "Erreur", response.get("message", "Erreur inconnue"))
