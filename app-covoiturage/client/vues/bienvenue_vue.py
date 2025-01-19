from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class PageBienvenue(QWidget):
    login_requested = pyqtSignal()
    register_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenue")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.login_button = QPushButton("Se connecter")
        self.register_button = QPushButton("Créer un compte")

        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        # Connecter les boutons aux signaux et fermer la fenêtre
        self.login_button.clicked.connect(self.emit_and_close_login)
        self.register_button.clicked.connect(self.emit_and_close_register)

    def emit_and_close_login(self):
        self.login_requested.emit()
        self.close()

    def emit_and_close_register(self):
        self.register_requested.emit()
        self.close()
