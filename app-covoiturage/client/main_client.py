import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication
from vues.bienvenue_vue import PageBienvenue
from vues.login_vue import PageLogin
from vues.register_vue import PageRegister
from vues.dashboard_vue import DashboardView
from vues.ajouter_trajet_vue import AjouterTrajetView
from vues.voir_trajets_vue import VoirTrajetsView
from vues.gerer_trajet_vue import GererTrajetView
from controllers.login_controller import LoginController
from controllers.register_controller import RegisterController
from controllers.trajet_controller import TrajetController
from controllers.gerer_trajet_controller import GererTrajetController


def main():
    app = QApplication(sys.argv)

    # Création des vues
    bienvenue_view = PageBienvenue()
    login_view = PageLogin()
    register_view = PageRegister(lambda: show_dashboard())
    dashboard_view = DashboardView()
    ajouter_trajet_view = AjouterTrajetView()
    voir_trajets_view = VoirTrajetsView()
    gerer_trajet_view = GererTrajetView()
    gerer_trajet_controller = GererTrajetController(gerer_trajet_view)

    # Méthode pour cacher toutes les fenêtres
    def hide_all_views():
        bienvenue_view.hide()
        login_view.hide()
        register_view.hide()
        dashboard_view.hide()
        ajouter_trajet_view.hide()
        voir_trajets_view.hide()
        gerer_trajet_view.hide()

    # Fonctions pour la navigation entre les vues
    def show_bienvenue():
        hide_all_views()
        bienvenue_view.show()

    def show_login():
        hide_all_views()
        login_view.show()

    def show_register():
        hide_all_views()
        register_view.show()

    def show_dashboard():
        hide_all_views()
        dashboard_view.show()

    def show_ajouter_trajet():
        hide_all_views()
        ajouter_trajet_view.show()

    def show_voir_trajets():
        hide_all_views()
        trajet_controller.fetch_trajets()
        voir_trajets_view.show()

    def show_gerer_trajet():
        hide_all_views()
        gerer_trajet_controller.actualiser_trajets()
        gerer_trajet_view.show()

    def logout():
        hide_all_views()
        bienvenue_view.show()

    # Création des contrôleurs
    login_controller = LoginController(login_view)
    register_controller = RegisterController(register_view, show_dashboard)
    trajet_controller = TrajetController(ajouter_trajet_view, voir_trajets_view)

    # Connexion des signaux
    bienvenue_view.login_requested.connect(show_login)
    bienvenue_view.register_requested.connect(show_register)
    login_controller.login_success.connect(show_dashboard)

    # Connexion des signaux aux méthodes appropriées
   # trajet_controller.ajouter_trajet_view.connect(show_dashboard)
   # trajet_controller.trajets_recuperes.connect(voir_trajets_view.display_trips)

    # Connexion des boutons du tableau de bord
    dashboard_view.view_trips_button.clicked.connect(show_voir_trajets)
    dashboard_view.add_trip_button.clicked.connect(show_ajouter_trajet)
    dashboard_view.gerer_trip_button.clicked.connect(show_gerer_trajet)
    dashboard_view.logout_button.clicked.connect(logout)

    # Boutons des vues secondaires
    ajouter_trajet_view.back_button.clicked.connect(show_dashboard)
    voir_trajets_view.back_button.clicked.connect(show_dashboard)
    gerer_trajet_view.back_button.clicked.connect(show_dashboard)

    # Affichage initial
    show_bienvenue()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
