from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
class AdminVue(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Panel")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()

        # Titre
        self.title_label = QLabel("Admin Panel")
        self.layout.addWidget(self.title_label)

        # Tableau des utilisateurs
        self.users_table = QTableWidget()
        self.layout.addWidget(self.users_table)

        # Boutons
        self.add_user_button = QPushButton("Ajouter un utilisateur")
        self.layout.addWidget(self.add_user_button)

        self.setLayout(self.layout)
