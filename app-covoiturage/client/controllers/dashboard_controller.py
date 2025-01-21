from PyQt5.QtWidgets import QApplication

class DashboardController:
    def __init__(self, dashboard_view, show_view_callback):
        """
        Initializes the dashboard controller.

        Args:
            dashboard_view: The view associated with the dashboard.
            show_view_callback: Function to display another view.
        """
        self.dashboard_view = dashboard_view
        self.show_view_callback = show_view_callback

        # Connecter les boutons aux méthodes
        self.dashboard_view.btn_voir_trajets.clicked.connect(self.voir_trajets)
        self.dashboard_view.btn_ajouter_trajet.clicked.connect(self.ajouter_trajet)
        self.dashboard_view.btn_deconnexion.clicked.connect(self.deconnexion)

    def voir_trajets(self):
        """
        Method triggered when "View available trips" is clicked.
        """
        self.show_view_callback("voir_trajets")

    def ajouter_trajet(self):
        """
        Method triggered when "Add a trip" is clicked.
        """
        self.show_view_callback("ajouter_trajet")

    def deconnexion(self):
        """
               Method triggered when "Log out" is clicked.
               Closes the application completely.
        """
        print("Déconnexion demandée. Fermeture de l'application.")
        QApplication.quit()  # Ferme l'application proprement
