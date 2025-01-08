from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class PageDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tableau de bord - Application de Covoiturage")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        # Message de bienvenue
        label = QLabel("Bienvenue dans le tableau de bord !")
        layout.addWidget(label)

        # Bouton de déconnexion
        btn_deconnexion = QPushButton("Se déconnecter")
        btn_deconnexion.clicked.connect(self.deconnexion)
        layout.addWidget(btn_deconnexion)

        self.setLayout(layout)

    def deconnexion(self):
        """Retourner à la page de sélection ou connexion."""
        if self.parent:
            self.parent.show_selection()
