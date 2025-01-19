class TrajetModel:
    def __init__(self, conn, depart, arrivee, date_heure, prix, places_disponibles):
            self.conn = conn
            self.depart = depart
            self.arrivee = arrivee
            self.date_heure = date_heure
            self.prix = prix
            self.places_disponibles = places_disponibles

    def to_json(self):
        return {
            "depart": self.depart,
            "arrivee": self.arrivee,
            "date_heure": self.date_heure,
            "prix": self.prix,
            "places_disponibles": self.places_disponibles
        }
