from PyQt5.QtWidgets import QApplication

class DashboardController:
    def __init__(self, dashboard_view, show_view_callback):
        """
        Initialise le contrôleur du tableau de bord.

        :param dashboard_view: Vue associée au tableau de bord.
        :param show_view_callback: Fonction pour afficher une autre vue.
        """
        self.dashboard_view = dashboard_view
        self.show_view_callback = show_view_callback

        # Connecter les boutons aux méthodes
        self.dashboard_view.btn_voir_trajets.clicked.connect(self.voir_trajets)
        self.dashboard_view.btn_ajouter_trajet.clicked.connect(self.ajouter_trajet)
        self.dashboard_view.btn_deconnexion.clicked.connect(self.deconnexion)

    def voir_trajets(self):
        """
        Méthode déclenchée lors du clic sur "Voir les trajets disponibles".
        """
        self.show_view_callback("voir_trajets")

    def ajouter_trajet(self):
        """
        Méthode déclenchée lors du clic sur "Ajouter un trajet".
        """
        self.show_view_callback("ajouter_trajet")

    def deconnexion(self):
        """
        Méthode déclenchée lors du clic sur "Se déconnecter".
        Ferme l'application complètement.
        """
        print("Déconnexion demandée. Fermeture de l'application.")
        QApplication.quit()  # Ferme l'application proprement
