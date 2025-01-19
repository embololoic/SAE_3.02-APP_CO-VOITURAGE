from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class DeconnexionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Se déconnecter")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Voulez-vous vraiment vous déconnecter ?")
        self.layout.addWidget(self.title_label)

        self.confirm_button = QPushButton("Oui")
        self.layout.addWidget(self.confirm_button)

        self.cancel_button = QPushButton("Non")
        self.layout.addWidget(self.cancel_button)

        self.setLayout(self.layout)