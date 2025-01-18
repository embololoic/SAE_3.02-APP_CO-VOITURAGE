import MySQLdb
from datetime import datetime

class BaseDonnees:
    def __init__(self, host="192.168.156.221", user="rsissako", password="Fatou7151@", database="rsissako1"):
        try:
            self.conn = MySQLdb.connect(
                host=host,
                user=user,
                passwd=password,
                db=database
            )
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
            print("Connexion établie avec la base de données MySQL.")
        except MySQLdb.Error as err:
            print(f"Erreur lors de la connexion à la base de données : {err}")
            self.conn = None

    def inserer_trajets(self):
        if not self.conn:
            print("La connexion à la base de données n'est pas établie.")
            return

        try:
            insert_query = """
            INSERT INTO trajets (depart, arrivee, date_heure, prix, places_disponibles, distance_km, impact_carbone, cout_total, description, etat) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            trajets = [
                ('Paris', 'Lyon', '2025-01-15 10:00:00', 30.0, 4, 465.0, 50.0, 100.0, 'Trajet rapide et confortable', 'en attente'),
                ('Marseille', 'Nice', '2025-02-20 14:00:00', 25.0, 3, 200.0, 30.0, 80.0, 'Trajet avec vue sur la mer', 'en attente'),
                ('Bordeaux', 'Toulouse', '2025-03-10 08:00:00', 20.0, 5, 250.0, 40.0, 90.0, 'Trajet agréable', 'en attente'),
                ('Lille', 'Bruxelles', '2025-04-05 12:00:00', 15.0, 2, 110.0, 20.0, 50.0, 'Trajet international', 'en attente'),
                ('Nantes', 'Rennes', '2025-05-18 09:00:00', 10.0, 6, 100.0, 10.0, 30.0, 'Trajet court', 'en attente')
            ]

            self.cursor.executemany(insert_query, trajets)
            self.conn.commit()
            print(f"{self.cursor.rowcount} trajets insérés avec succès.")

        except MySQLdb.Error as err:
            print(f"Erreur lors de l'insertion des trajets : {err}")
            self.conn.rollback()

    def fermer_connexion(self):
        if self.conn:
            self.conn.close()
            print("Connexion à la base de données fermée.")

if __name__ == "__main__":
    db = BaseDonnees()
    db.inserer_trajets()
    db.fermer_connexion()
