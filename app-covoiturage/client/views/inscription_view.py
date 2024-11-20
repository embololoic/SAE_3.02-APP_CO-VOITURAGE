# client/views/inscription_view.py
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class InscriptionView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        # Création des widgets
        layout = QFormLayout()

        # Champs de saisie de données
        self.nom = QLineEdit(self)
        self.prenom = QLineEdit(self)
        self.login = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)  # Masquer le mot de passe
        self.adresse = QLineEdit(self)
        self.telephone = QLineEdit(self)
        self.edt = QLineEdit(self)  # Lien vers l'emploi du temps
        self.places = QLineEdit(self)
        self.cv_fiscaux = QLineEdit(self)
        self.indisponibilites = QLineEdit(self)

        # Ajouter les champs au formulaire
        layout.addRow("Nom:", self.nom)
        layout.addRow("Prénom:", self.prenom)
        layout.addRow("Login:", self.login)
        layout.addRow("Mot de passe:", self.password)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Téléphone:", self.telephone)
        layout.addRow("Emploi du temps:", self.edt)
        layout.addRow("Nombre de places:", self.places)
        layout.addRow("CV fiscaux:", self.cv_fiscaux)
        layout.addRow("Indisponibilités:", self.indisponibilites)

        # Bouton pour soumettre
        submit_button = QPushButton("S'inscrire")
        submit_button.clicked.connect(self.controller.handle_submit)

        # Bouton pour annuler
        cancel_button = QPushButton("Annuler")
        cancel_button.clicked.connect(self.controller.handle_cancel)

        # Ajouter les boutons
        layout.addWidget(submit_button)
        layout.addWidget(cancel_button)

        self.setLayout(layout)
        self.setWindowTitle("Inscription")
        self.setGeometry(300, 300, 400, 400)
        self.show()

