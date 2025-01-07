#index.py
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from PyQt5.QtCore import Qt
from app_covoiturage.vue.login import PageLogin
from app_covoiturage.vue.register import PageRegister

class PageIndex(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Accueil - Application de Covoiturage")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        layout = QVBoxLayout()

        # Message d'accueil
        self.label_welcome = QLabel("Bienvenue dans l'application de covoiturage")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_welcome)

        # Bouton pour se connecter
        self.btn_connexion = QPushButton("Se connecter")
        layout.addWidget(self.btn_connexion)

        # Bouton pour créer un compte
        self.btn_inscription = QPushButton("Créer un compte")
        layout.addWidget(self.btn_inscription)

        # Appliquer le layout
        self.setLayout(layout)

# Application principale
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Créer les pages
    page_index = PageIndex()
    page_login = PageLogin()
    page_register = PageRegister()

    # Connecter les boutons aux actions
    page_index.btn_connexion.clicked.connect(lambda: (page_index.hide(), page_login.show()))
    page_index.btn_inscription.clicked.connect(lambda: (page_index.hide(), page_register.show()))
    page_login.btn_connexion.clicked.connect(lambda: (page_login.hide(), page_index.show()))
    page_register.btn_inscription.clicked.connect(lambda: (page_register.hide(), page_index.show()))

    # Afficher la page d'accueil
    page_index.show()

    sys.exit(app.exec_())
