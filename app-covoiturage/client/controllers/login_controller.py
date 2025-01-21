import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from client.utils.protocole import send_request

class LoginController(QObject):
    login_success = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.view.btn_login.clicked.connect(self.login_utilisateur)

    def login_utilisateur(self):
        """
        Handles the user login process.

        Collects the email and password from the view, sends a login request to the server,
        and processes the server's response.

        Parameters:
        None

        Returns:
        None
        """
        data = {
            "email": self.view.input_email.text(),
            "password": self.view.input_password.text()
        }

        response = send_request("login", data)
        if response and response.get("status") == "success":
            user_data = response.get("user")  # Récupération du dictionnaire 'user'
            user_id = user_data.get("id")  # Extraction de l'ID utilisateur
            QMessageBox.information(self.view, "Succès", f"Connexion réussie! ID utilisateur: {user_id}")

            self.login_success.emit()  # Signal de succès pour redirection
        else:
            QMessageBox.critical(self.view, "Erreur", "Erreur lors de la connexion.")
