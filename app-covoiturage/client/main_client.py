# client/main_client.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication
from vues.bienvenue_vue import PageBienvenue
from vues.login_vue import PageLogin
from vues.register_vue import PageRegister
from controllers.login_controller import LoginController
from controllers.register_controller import RegisterController
from vues.dashboard_vue import Dashboard



def main():
    app = QApplication(sys.argv)

    # Création des vues
    bienvenue_view = PageBienvenue()
    login_view = PageLogin()
    dashboard_view = Dashboard()

    def show_login():
        bienvenue_view.close()  # Ferme la page de bienvenue
        login_view.show()       # Affiche la page de connexion

    def show_register():
        bienvenue_view.close()  # Ferme la page de bienvenue
        register_view.show()    # Affiche la page d'inscription

    def show_dashboard():
        login_view.close()      # Ferme la page de connexion
        dashboard_view.show()   # Affiche le tableau de bord

    # Création des contrôleurs
    login_controller = LoginController(login_view)
    register_view = PageRegister(show_dashboard)
    register_controller = RegisterController(register_view, show_dashboard)

    # Connexion des signaux
    bienvenue_view.login_requested.connect(show_login)
    bienvenue_view.register_requested.connect(show_register)
    login_controller.login_success.connect(show_dashboard)

    # Affichage initial
    bienvenue_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()