from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class PageAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Administration - Application de Covoiturage")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.label_bienvenue = QLabel("Bienvenue dans l'interface administrateur")
        layout.addWidget(self.label_bienvenue)

        self.btn_utilisateurs = QPushButton("Gérer les utilisateurs")
        layout.addWidget(self.btn_utilisateurs)

        self.btn_trajets = QPushButton("Gérer les trajets")
        layout.addWidget(self.btn_trajets)

        self.btn_stats = QPushButton("Voir les statistiques")
        layout.addWidget(self.btn_stats)

        self.setLayout(layout)
