import sys
import os
# Ajout du chemin de `app-covoiturage` au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMessageBox, QPushButton, QWidget, QVBoxLayout, QLabel
from client.vues.login import PageLogin
from client.vues.register import PageRegister
from client.vues.dashboard import PageDashboard  # Page principale après connexion

class AppManager(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Initialiser les pages
        self.page_selection = PageSelection(self)
        self.page_login = PageLogin(self)
        self.page_register = PageRegister(self)
        self.page_dashboard = PageDashboard(self)

        # Ajouter les pages au gestionnaire
        self.addWidget(self.page_selection)
        self.addWidget(self.page_login)
        self.addWidget(self.page_register)
        self.addWidget(self.page_dashboard)

        # Charger la page de sélection par défaut
        self.setCurrentWidget(self.page_selection)

        print("Initialisation du protocole...")
        print("Connexion établie avec la base de données...")
        print("Ouverture du port pour les communications...")

    def show_selection(self):
        """Afficher la page de sélection (connexion ou inscription)."""
        self.setCurrentWidget(self.page_selection)

    def show_login(self):
        """Afficher la page de connexion."""
        self.setCurrentWidget(self.page_login)

    def show_register(self):
        """Afficher la page d'inscription."""
        self.setCurrentWidget(self.page_register)

    def show_dashboard(self):
        """Afficher la page principale après connexion."""
        self.setCurrentWidget(self.page_dashboard)

class PageSelection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bienvenue - Application de Covoiturage")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Message d'accueil
        label = QLabel("Bienvenue dans l'application de covoiturage !")
        layout.addWidget(label)

        # Bouton pour se connecter
        btn_connexion = QPushButton("Se connecter")
        btn_connexion.clicked.connect(self.go_to_login)
        layout.addWidget(btn_connexion)

        # Bouton pour créer un compte
        btn_inscription = QPushButton("Créer un compte")
        btn_inscription.clicked.connect(self.go_to_register)
        layout.addWidget(btn_inscription)

        self.setLayout(layout)

    def go_to_login(self):
        if self.parent:
            self.parent.show_login()

    def go_to_register(self):
        if self.parent:
            self.parent.show_register()

def main():
    try:
        app = QApplication(sys.argv)

        # Initialiser le gestionnaire d'application
        manager = AppManager()
        manager.show()

        sys.exit(app.exec_())
    except Exception as e:
        print(f"Erreur critique : {e}")
        QMessageBox.critical(None, "Erreur critique", "Une erreur critique est survenue. Veuillez contacter le support.")

if __name__ == "__main__":
    main()
