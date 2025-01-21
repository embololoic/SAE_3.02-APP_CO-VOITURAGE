from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
import datetime

def get_current_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class AjouterTrajetView(QWidget):
    """
    Vue pour ajouter un nouveau trajet.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter un trajet")
        self.setGeometry(100, 100, 600, 800)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Ajouter un nouveau trajet")
        self.layout.addWidget(self.title_label)

        self.conducteur_id_label = QLabel("ID du conducteur :")
        self.layout.addWidget(self.conducteur_id_label)
        self.conducteur_id_input = QLineEdit()
        self.layout.addWidget(self.conducteur_id_input)

        self.depart_label = QLabel("Lieu de départ :")
        self.layout.addWidget(self.depart_label)
        self.depart_input = QLineEdit()
        self.layout.addWidget(self.depart_input)

        self.destination_label = QLabel("Lieu de destination :")
        self.layout.addWidget(self.destination_label)
        self.destination_input = QLineEdit()
        self.layout.addWidget(self.destination_input)

        self.date_label = QLabel("Date du trajet :")
        self.layout.addWidget(self.date_label)
        self.date_input = QLineEdit()
        self.date_input.setText(get_current_datetime())
        self.layout.addWidget(self.date_input)

        self.prix_label = QLabel("Prix :")
        self.layout.addWidget(self.prix_label)
        self.prix_input = QLineEdit()
        self.layout.addWidget(self.prix_input)

        self.places_label = QLabel("Places disponibles :")
        self.layout.addWidget(self.places_label)
        self.places_input = QLineEdit()
        self.layout.addWidget(self.places_input)

        self.distance_label = QLabel("Distance (km) :")
        self.layout.addWidget(self.distance_label)
        self.distance_input = QLineEdit()
        self.layout.addWidget(self.distance_input)

        self.cout_total_label = QLabel("Coût total :")
        self.layout.addWidget(self.cout_total_label)
        self.cout_total_input = QLineEdit()
        self.layout.addWidget(self.cout_total_input)

        self.description_label = QLabel("Description :")
        self.layout.addWidget(self.description_label)
        self.description_input = QTextEdit()
        self.layout.addWidget(self.description_input)

        self.add_button = QPushButton("Ajouter")
        self.layout.addWidget(self.add_button)

        self.back_button = QPushButton("Retour")
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        # Connect events
        self.prix_input.textChanged.connect(self.update_cout_total)
        self.places_input.textChanged.connect(self.update_cout_total)

    def update_cout_total(self):
        """
        Met à jour dynamiquement le coût total en fonction du prix et des places.
        """
        try:
            prix = float(self.prix_input.text())
            places = int(self.places_input.text())
            cout_total = prix * places
            self.cout_total_input.setText(str(cout_total))
            print(f"[LOG] Coût total mis à jour : {cout_total}")
        except ValueError:
            self.cout_total_input.setText("")
            print("[LOG] Erreur lors du calcul du coût total (valeurs invalides).")
