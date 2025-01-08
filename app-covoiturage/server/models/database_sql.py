import MySQLdb

class BaseDonnees:
    def __init__(self, host="localhost", user="root", password="", database="covoiturage"):
        try:
            self.conn = MySQLdb.connect(
                host=host,
                user=user,
                passwd=password,
                db=database
            )
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
            print("Connexion réussie à la base de données.")
        except MySQLdb.Error as e:
            print(f"Erreur de connexion : {e}")
            self.conn = None

    def fermer_connexion(self):
        if self.conn:
            self.conn.close()
