# client/main_client.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication
from vues.bienvenue_vue import PageBienvenue
from vues.login_vue import PageLogin
from vues.register_vue import PageRegister
from vues.dashboard_vue import Dashboard
from vues.ajouter_trajet_vue import AjouterTrajetView
from vues.voir_trajets_vue import VoirTrajetsView
from controllers.login_controller import LoginController
from controllers.register_controller import RegisterController


def main():
    app = QApplication(sys.argv)

    # Création des vues
    bienvenue_view = PageBienvenue()
    login_view = PageLogin()
    dashboard_view = Dashboard()
    ajouter_trajet_view = AjouterTrajetView()
    voir_trajets_view = VoirTrajetsView()

    # Navigation entre les vues
    def show_login():
        bienvenue_view.close()
        login_view.show()

    def show_register():
        bienvenue_view.close()
        register_view.show()

    def show_dashboard():
        login_view.close()
        ajouter_trajet_view.close()
        voir_trajets_view.close()
        dashboard_view.show()

    def show_ajouter_trajet():
        dashboard_view.close()
        ajouter_trajet_view.show()

    def show_voir_trajets():
        dashboard_view.close()
        voir_trajets_view.show()

    def logout():
        dashboard_view.close()
        bienvenue_view.show()

    # Instanciation de la vue Register avec la fonction de callback
    register_view = PageRegister(show_dashboard)

    # Création des contrôleurs
    login_controller = LoginController(login_view)
    register_controller = RegisterController(register_view, show_dashboard)

    # Connexion des signaux
    bienvenue_view.login_requested.connect(show_login)
    bienvenue_view.register_requested.connect(show_register)
    login_controller.login_success.connect(show_dashboard)

    # Connexion des boutons du tableau de bord
    dashboard_view.view_trips_button.clicked.connect(show_voir_trajets)
    dashboard_view.add_trip_button.clicked.connect(show_ajouter_trajet)
    dashboard_view.logout_button.clicked.connect(logout)

    # Boutons des vues secondaires
    ajouter_trajet_view.back_button.clicked.connect(show_dashboard)
    voir_trajets_view.back_button.clicked.connect(show_dashboard)

    # Affichage initial
    bienvenue_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
