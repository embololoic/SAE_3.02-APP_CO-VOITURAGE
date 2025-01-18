from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AjouterTrajetView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter un trajet")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Ajouter un nouveau trajet")
        self.layout.addWidget(self.title_label)

        self.depart_label = QLabel("Lieu de départ :")
        self.layout.addWidget(self.depart_label)
        self.depart_input = QLineEdit()
        self.layout.addWidget(self.depart_input)

        self.destination_label = QLabel("Lieu de destination :")
        self.layout.addWidget(self.destination_label)
        self.destination_input = QLineEdit()
        self.layout.addWidget(self.destination_input)

        self.date_label = QLabel("Date du trajet :")
        self.layout.addWidget(self.date_label)
        self.date_input = QLineEdit()
        self.layout.addWidget(self.date_input)

        self.add_button = QPushButton("Ajouter")
        self.layout.addWidget(self.add_button)

        self.back_button = QPushButton("Retour")
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)