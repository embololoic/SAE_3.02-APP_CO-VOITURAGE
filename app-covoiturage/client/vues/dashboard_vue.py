from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class Dashboard(QWidget):
    def __init__(self):
        """
        Initializes the Dashboard.

        Sets up the window title, geometry, and layout. Adds labels for the title and personal statistics,
        and buttons for viewing available trips, adding a new trip, and logging out.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()

        # Titre
        self.title_label = QLabel("Bienvenue sur votre Dashboard")
        self.layout.addWidget(self.title_label)

        # Statistiques
        self.stats_label = QLabel("Statistiques personnelles :")
        self.layout.addWidget(self.stats_label)

        # Bouton pour voir les trajets
        self.view_trips_button = QPushButton("Voir les trajets disponibles")
        self.layout.addWidget(self.view_trips_button)

        # Bouton pour ajouter un trajet
        self.add_trip_button = QPushButton("Ajouter un trajet")
        self.layout.addWidget(self.add_trip_button)

        # Bout
        self.logout_button = QPushButton("Se déconnecter")
        self.layout.addWidget(self.logout_button)


        self.setLayout(self.layout)
