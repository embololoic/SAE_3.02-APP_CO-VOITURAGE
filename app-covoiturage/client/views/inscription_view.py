# client/views/inscription_view.py
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton


class InscriptionView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        layout = QFormLayout()

        self.nom = QLineEdit()
        self.prenom = QLineEdit()
        self.login = QLineEdit()
        self.password = QLineEdit()
        self.adresse = QLineEdit()
        self.telephone = QLineEdit()
        self.edt = QLineEdit()  # Lien vers le fichier d'Emploi du Temps
        self.places = QLineEdit()
        self.cv_fiscaux = QLineEdit()
        self.indisponibilites = QLineEdit()

        layout.addRow("Nom:", self.nom)
        layout.addRow("Prénom:", self.prenom)
        layout.addRow("Login:", self.login)
        layout.addRow("Password:", self.password)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Téléphone:", self.telephone)
        layout.addRow("Emploi du temps:", self.edt)
        layout.addRow("Nombre de places:", self.places)
        layout.addRow("CV fiscaux:", self.cv_fiscaux)
        layout.addRow("Jours d'indisponibilité:", self.indisponibilites)

        submit_button = QPushButton("S'inscrire")
        submit_button.clicked.connect(self.controller.create_account)
        layout.addWidget(submit_button)

        self.setLayout(layout)
