from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from client.controllers.login_controller import LoginController

class PageLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # Passer le parent au constructeur de QWidget
        self.parent = parent  # Stocker une référence au parent (AppManager)
        self.controller = LoginController()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Connexion - Application de Covoiturage")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label_email = QLabel("Email :")
        layout.addWidget(self.label_email)
        self.input_email = QLineEdit()
        layout.addWidget(self.input_email)

        self.label_password = QLabel("Mot de passe :")
        layout.addWidget(self.label_password)
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)

        self.btn_connexion = QPushButton("Se connecter")
        self.btn_connexion.clicked.connect(self.se_connecter)
        layout.addWidget(self.btn_connexion)

        self.setLayout(layout)

    def se_connecter(self):
        """Vérifie les identifiants et navigue vers l'accueil en cas de succès."""
        email = self.input_email.text()
        mot_de_passe = self.input_password.text()

        response = self.controller.verifier_identifiants(email, mot_de_passe)

        if response.get("status") == "success":
            QMessageBox.information(self, "Connexion réussie", "Bienvenue !")
            if self.parent:
                self.parent.show_index()  # Navigation vers la page d'accueil
        else:
            QMessageBox.warning(self, "Erreur", response.get("message", "Erreur inconnue"))
