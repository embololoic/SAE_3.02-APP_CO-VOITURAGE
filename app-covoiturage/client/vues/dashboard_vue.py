from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tableau de bord")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.view_trips_button = QPushButton("Voir les trajets", self)
        self.view_trips_button.clicked.connect(self.log_view_trips)
        layout.addWidget(self.view_trips_button)

        self.add_trip_button = QPushButton("Ajouter un trajet", self)
        self.add_trip_button.clicked.connect(self.log_add_trip)
        layout.addWidget(self.add_trip_button)

        self.gerer_trip_button = QPushButton("Gérer les trajets", self)
        self.gerer_trip_button.clicked.connect(self.log_gerer_trips)
        layout.addWidget(self.gerer_trip_button)

        self.logout_button = QPushButton("Déconnexion", self)
        self.logout_button.clicked.connect(self.log_logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def log_view_trips(self):
        print("Page 'Voir les trajets' ouverte")

    def log_add_trip(self):
        print("Page 'Ajouter un trajet' ouverte")

    def log_gerer_trips(self):
        print("Page 'Gérer les trajets' ouverte")

    def log_logout(self):
        print("Déconnexion")