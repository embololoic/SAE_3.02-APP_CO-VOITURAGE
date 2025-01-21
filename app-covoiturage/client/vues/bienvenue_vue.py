
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication

class PageBienvenue(QWidget):
    login_requested = pyqtSignal()
    register_requested = pyqtSignal()

    def __init__(self):
        """
        Initializes the PageBienvenue.

        Sets up the window title, geometry, and layout. Adds buttons for login and registration,
        and connects them to their respective signals.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()
        self.setWindowTitle("Bienvenue")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.login_button = QPushButton("Se connecter")
        self.register_button = QPushButton("Créer un compte")
        self.quit_button = QPushButton("Quitter l'application")

        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

        # Connecter les boutons aux signaux et fermer la fenêtre
        self.login_button.clicked.connect(self.emit_and_close_login)
        self.register_button.clicked.connect(self.emit_and_close_register)
        self.quit_button.clicked.connect(QApplication.quit)

    def emit_and_close_login(self):
        self.login_requested.emit()
        self.close()

    def emit_and_close_register(self):
        self.register_requested.emit()
        self.close()