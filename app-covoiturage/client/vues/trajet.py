from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class PageTrajet(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Trajets - Application de Covoiturage")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        # Recherche de trajets
        self.label_recherche = QLabel("Rechercher un trajet :")
        layout.addWidget(self.label_recherche)
        self.input_depart = QLineEdit()
        self.input_depart.setPlaceholderText("Lieu de départ")
        layout.addWidget(self.input_depart)

        self.input_arrivee = QLineEdit()
        self.input_arrivee.setPlaceholderText("Lieu d'arrivée")
        layout.addWidget(self.input_arrivee)

        self.btn_recherche = QPushButton("Rechercher")
        layout.addWidget(self.btn_recherche)

        # Proposition de trajets
        layout.addWidget(QLabel("Proposer un trajet :"))
        self.input_depart_proposer = QLineEdit()
        self.input_depart_proposer.setPlaceholderText("Lieu de départ")
        layout.addWidget(self.input_depart_proposer)

        self.input_arrivee_proposer = QLineEdit()
        self.input_arrivee_proposer.setPlaceholderText("Lieu d'arrivée")
        layout.addWidget(self.input_arrivee_proposer)

        self.btn_proposer = QPushButton("Proposer")
        layout.addWidget(self.btn_proposer)

        self.setLayout(layout)
