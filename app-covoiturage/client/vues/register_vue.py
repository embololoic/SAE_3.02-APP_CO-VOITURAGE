import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox, QHBoxLayout, QFileDialog, QMessageBox
from client.controllers.register_controller import RegisterController


class PageRegister(QWidget):
    def __init__(self, show_dashboard_callback):
        """
        Initializes the PageRegister.

        Calls the setup_ui method to set up the window title, geometry, and layout. Adds labels and input fields
        for name, surname, email, password, and other registration details. Also adds a button to submit the registration information.

        Parameters:
        show_dashboard_callback (function): Callback function to show the dashboard after successful registration.

        Returns:
        None
        """
        super().__init__()
        self.setup_ui()
        self.controller = RegisterController(self, show_dashboard_callback)

    def setup_ui(self):
        """
        Sets up the user interface for the registration page.

        Configures the window title, geometry, and layout. Adds labels and input fields
        for name, surname, email, password, and other registration details. Also adds a button to submit the registration information.

        Parameters:
        None

        Returns:
        None
        """
        self.setWindowTitle("Inscription - Application de Covoiturage")
        self.setGeometry(100, 100, 500, 800)

        layout = QVBoxLayout()

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

        self.label_adresse = QLabel("Adresse :")
        layout.addWidget(self.label_adresse)
        self.input_adresse = QLineEdit()
        self.input_adresse.setPlaceholderText("Entrez votre adresse")
        layout.addWidget(self.input_adresse)

        self.label_gps = QLabel("Coordonnées GPS :")
        layout.addWidget(self.label_gps)
        self.input_gps = QLineEdit()
        self.input_gps.setPlaceholderText("Entrez vos coordonnées GPS")
        layout.addWidget(self.input_gps)

        self.label_places = QLabel("Nombre de places dans la voiture :")
        layout.addWidget(self.label_places)
        self.input_places = QSpinBox()
        self.input_places.setMinimum(1)
        self.input_places.setMaximum(9)
        layout.addWidget(self.input_places)

        self.label_cv = QLabel("CV fiscaux :")
        layout.addWidget(self.label_cv)
        self.input_cv = QSpinBox()
        self.input_cv.setMinimum(1)
        self.input_cv.setMaximum(20)
        layout.addWidget(self.input_cv)

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

        self.label_calendar = QLabel("Emploi du temps (iCalendar) :")
        layout.addWidget(self.label_calendar)
        self.btn_calendar = QPushButton("Choisir un fichier")
        self.btn_calendar.clicked.connect(self.choisir_fichier)
        layout.addWidget(self.btn_calendar)

        self.btn_inscription = QPushButton("S'inscrire")
        layout.addWidget(self.btn_inscription)

        self.setLayout(layout)

    def choisir_fichier(self):
        fichier, _ = QFileDialog.getOpenFileName(self, "Sélectionner un fichier iCalendar", "", "Fichiers iCalendar (*.ics)")
        if fichier:
            self.label_calendar.setText(f"Fichier sélectionné : {fichier}")
