### Updated TrajetView with Calendar and Dropdown ###
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,
    QDateTimeEdit, QSpinBox, QDoubleSpinBox
)
from PyQt5.QtCore import QDateTime

class TrajetView(QWidget):
    def __init__(self):
        """
        Initializes the TrajetView.

        Sets up the window title, geometry, and layout. Adds labels and input fields
        for departure location, arrival location, date and time, price, and available seats.
        Also adds a button to submit the new trip.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()
        self.setWindowTitle("Ajouter un trajet")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.depart_label = QLabel("Depart:")
        self.depart_input = QLineEdit()
        self.layout.addWidget(self.depart_label)
        self.layout.addWidget(self.depart_input)

        self.arrivee_label = QLabel("Arrivée:")
        self.arrivee_input = QLineEdit()
        self.layout.addWidget(self.arrivee_label)
        self.layout.addWidget(self.arrivee_input)

        self.date_heure_label = QLabel("Date/heure:")
        self.date_heure_input = QDateTimeEdit()
        self.date_heure_input.setCalendarPopup(True)
        self.date_heure_input.setDateTime(QDateTime.currentDateTime())
        self.layout.addWidget(self.date_heure_label)
        self.layout.addWidget(self.date_heure_input)

        self.prix_label = QLabel("Prix:")
        self.prix_input = QDoubleSpinBox()
        self.prix_input.setRange(0, 1000)
        self.prix_input.setSuffix(" €")
        self.layout.addWidget(self.prix_label)
        self.layout.addWidget(self.prix_input)

        self.places_label = QLabel("Sieges disponibles:")
        self.places_input = QSpinBox()
        self.places_input.setRange(1, 50)
        self.layout.addWidget(self.places_label)
        self.layout.addWidget(self.places_input)

        self.submit_button = QPushButton("Sousmettre")
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def show_success_message(self):
        QMessageBox.information(self, "Reussi", "Trajet ajouté avec succès!")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Erreur", message)