from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PageLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Connexion - Application de Covoiturage")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.label_email = QLabel("Email :")
        layout.addWidget(self.label_email)
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Entrez votre email")
        layout.addWidget(self.input_email)

        self.label_password = QLabel("Mot de passe :")
        layout.addWidget(self.label_password)
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Entrez votre mot de passe")
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)

        self.btn_login = QPushButton("Se connecter")
        layout.addWidget(self.btn_login)

        self.setLayout(layout)