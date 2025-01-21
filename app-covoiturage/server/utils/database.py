import MySQLdb

class BaseDonnees:
    """
    Classe pour gérer la connexion à la base de données MySQL et effectuer des opérations telles que
    la création de tables, la suppression conditionnelle des tables existantes, et la fermeture de connexion.
    """

    def __init__(self, host="192.168.156.221", user="rsissako", password="Fatou7151@", database="covoiturage"):
        """
        Initialise une connexion à la base de données MySQL.

        Args:
            host (str): L'adresse du serveur MySQL (par défaut "localhost").
            user (str): Le nom d'utilisateur MySQL (par défaut "root").
            password (str): Le mot de passe de l'utilisateur MySQL (par défaut vide).
            database (str): Le nom de la base de données à utiliser (par défaut "covoiturage").
        """
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

    
    def creer_tables(self, drop_existing=False):
        if not self.conn:
            print("La connexion à la base de données n'est pas établie.")
            return

        try:
            if drop_existing:
                print("Suppression des tables existantes...")
                self.cursor.execute("DROP TABLE IF EXISTS reservations")
                self.cursor.execute("DROP TABLE IF EXISTS trajets")
                self.cursor.execute("DROP TABLE IF EXISTS utilisateurs")
                print("Tables existantes supprimées.")

            # Table des utilisateurs
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                prenom VARCHAR(100) NOT NULL,
                email VARCHAR(191) UNIQUE NOT NULL,
                mot_de_passe VARCHAR(255) NOT NULL,
                adresse TEXT,
                coordonnees_gps VARCHAR(255),
                places_voiture INT,
                cv_fiscaux INT,
                indisponibilites TEXT,
                emploi_du_temps TEXT,
                role ENUM('user', 'admin') DEFAULT 'user'
            )
            ''')

            # Table des trajets
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS trajets (
                trajet_id INT AUTO_INCREMENT PRIMARY KEY,
                conducteur_id INT NOT NULL,
                depart VARCHAR(255) NOT NULL,
                arrivee VARCHAR(255) NOT NULL,
                date_heure DATETIME NOT NULL,
                prix FLOAT NOT NULL,
                places_disponibles INT NOT NULL,
                distance_km FLOAT DEFAULT 0,
                impact_carbone FLOAT DEFAULT 0,
                cout_total FLOAT DEFAULT 0,
                description TEXT,
                etat ENUM('en attente', 'en cours', 'termine') DEFAULT 'en attente',
                FOREIGN KEY (conducteur_id) REFERENCES utilisateurs (id)
            )
            ''')

            # Table des réservations
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                utilisateur_id INT NOT NULL,
                trajet_id INT NOT NULL,
                etat VARCHAR(50) DEFAULT 'en attente',
                date_reservation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs (id),
                FOREIGN KEY (trajet_id) REFERENCES trajets (id)
            )
            ''')

            self.conn.commit()
            print("Tables créées avec succès.")

        except MySQLdb.Error as err:
            print(f"Erreur lors de la création des tables : {err}")




    def fermer_connexion(self):
        """
        Ferme la connexion à la base de données MySQL.
        """
        if self.conn:
            try:
                self.conn.close()
                print("Connexion à la base de données fermée.")
            except MySQLdb.Error as err:
                print(f"Erreur lors de la fermeture de la connexion : {err}")

if __name__ == "__main__":
    # Exemple d'utilisation
    db = BaseDonnees(host="192.168.156.221", user="rsissako", password="Fatou7151@", database="rsissako1")
    db.creer_tables(drop_existing=True)  # Met drop_existing à True pour recréer les tables
    db.fermer_connexion()
