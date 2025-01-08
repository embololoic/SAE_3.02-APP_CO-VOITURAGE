class Trajet:
    def __init__(self, conducteur, depart, arrivee, date, prix, places_disponibles):
        self.conducteur = conducteur
        self.depart = depart
        self.arrivee = arrivee
        self.date = date
        self.prix = prix
        self.places_disponibles = places_disponibles

    def to_dict(self):
        """Convertit le trajet en dictionnaire."""
        return {
            "conducteur": self.conducteur,
            "depart": self.depart,
            "arrivee": self.arrivee,
            "date": self.date,
            "prix": self.prix,
            "places_disponibles": self.places_disponibles,
        }
