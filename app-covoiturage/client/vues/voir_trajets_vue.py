from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton

class VoirTrajetsView(QWidget):
    def __init__(self):
        """
        Initializes the VoirTrajetsView.

        Sets up the window title, geometry, and layout. Adds a label for the title,
        a table to display available trips, and a button to go back.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()
        self.setWindowTitle("Voir les trajets disponibles")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Trajets disponibles")
        self.layout.addWidget(self.title_label)

        self.trips_table = QTableWidget()
        self.layout.addWidget(self.trips_table)

        self.back_button = QPushButton("Retour")
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)