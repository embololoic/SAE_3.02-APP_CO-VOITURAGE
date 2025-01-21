from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox

class GererTrajetView(QWidget):
    """
    Vue pour gérer les trajets.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gérer les trajets")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        # Table pour afficher les trajets
        self.trajets_table = QTableWidget()
        self.trajets_table.setColumnCount(6)
        self.trajets_table.setHorizontalHeaderLabels([
            "trajet_id", "Départ", "Arrivée", "Date/Heure", "Prix (€)", "Places"
        ])
        self.layout.addWidget(self.trajets_table)

        # Boutons
        self.delete_button = QPushButton("Supprimer le trajet sélectionné")
        self.refresh_button = QPushButton("Actualiser la liste")
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.refresh_button)

        self.back_button = QPushButton("Retour")
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def populate_table(self, trajets):
        """
        Remplit la table avec les données des trajets.

        :param trajets: Liste des trajets (dict).
        """
        self.trajets_table.setRowCount(len(trajets))
        for row, trajet in enumerate(trajets):
            self.trajets_table.setItem(row, 0, QTableWidgetItem(str(trajet["trajet_id"])))
            self.trajets_table.setItem(row, 1, QTableWidgetItem(trajet["depart"]))
            self.trajets_table.setItem(row, 2, QTableWidgetItem(trajet["arrivee"]))
            self.trajets_table.setItem(row, 3, QTableWidgetItem(trajet["date_heure"]))
            self.trajets_table.setItem(row, 4, QTableWidgetItem(f"{trajet['prix']} €"))
            self.trajets_table.setItem(row, 5, QTableWidgetItem(str(trajet["places_disponibles"])))

    def get_selected_trajet_id(self):
        """
        Récupère l'ID du trajet sélectionné dans la table.

        :return: ID du trajet sélectionné ou None.
        """
        selected_row = self.trajets_table.currentRow()
        if selected_row != -1:
            return int(self.trajets_table.item(selected_row, 0).text())
        return None
