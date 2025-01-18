from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from vues.voir_trajets_vue import VoirTrajetsView
from vues.ajouter_trajet_vue import AjouterTrajetView
from vues.deconnexion_vue import DeconnexionView

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tableau de bord")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Bienvenue sur le tableau de bord")
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

        # Bouton pour se déconnecter
        self.logout_button = QPushButton("Se déconnecter")
        self.layout.addWidget(self.logout_button)

        self.setLayout(self.layout)

        # Connect buttons to their respective slots
        self.view_trips_button.clicked.connect(self.show_voir_trajets)
        self.add_trip_button.clicked.connect(self.show_ajouter_trajet)
        self.logout_button.clicked.connect(self.show_deconnexion)

    def show_voir_trajets(self):
        self.voir_trajets_view = VoirTrajetsView()
        self.voir_trajets_view.show()

    def show_ajouter_trajet(self):
        self.ajouter_trajet_view = AjouterTrajetView()
        self.ajouter_trajet_view.show()

    def show_deconnexion(self):
        self.deconnexion_view = DeconnexionView()
        self.deconnexion_view.show()
