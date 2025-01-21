from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton

class GererTrajetView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gérer les trajets")
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Liste des trajets", self)
        layout.addWidget(self.label)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Départ", "Arrivée", "Date/Heure", "Prix", "Places"])
        layout.addWidget(self.table)

        self.back_button = QPushButton("Retour", self)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def populate_table(self, trajets):
        self.table.setRowCount(len(trajets))
        for row, trajet in enumerate(trajets):
            self.table.setItem(row, 0, QTableWidgetItem(trajet["depart"]))
            self.table.setItem(row, 1, QTableWidgetItem(trajet["arrivee"]))
            self.table.setItem(row, 2, QTableWidgetItem(trajet["date"]))
            self.table.setItem(row, 3, QTableWidgetItem(str(trajet["prix"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(trajet["places"])))