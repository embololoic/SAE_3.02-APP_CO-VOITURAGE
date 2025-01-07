import MySQLdb

class BaseDonnees:
    def __init__(self, host="192.168.156.221", user="rsissako", password="Fatou7151@", database="rsissako1"):
        """Initialise la connexion à la base de données MySQL."""
        try:
            self.conn = MySQLdb.connect(
                host=host,
                user=user,
                passwd=password,
                db=database
            )
            self.cursor = self.conn.cursor()
            print("Connexion réussie à la base de données MySQL !")
        except MySQLdb.Error as err:
            print(f"Erreur : {err}")
            self.conn = None

    def creer_tables(self):
        """Crée les tables nécessaires pour l'application."""
        if not self.conn:
            print("La connexion à la base de données n'est pas établie.")
            return

        # Table des utilisateurs
        self.cursor.execute("""
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
        """)

        # Table des trajets
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS trajets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            conducteur_id INT NOT NULL,
            depart VARCHAR(255) NOT NULL,
            arrivee VARCHAR(255) NOT NULL,
            date_heure DATETIME NOT NULL,
            prix FLOAT NOT NULL,
            places_disponibles INT NOT NULL,
            distance_km FLOAT DEFAULT 0,
            impact_carbone FLOAT DEFAULT 0,
            cout_total FLOAT DEFAULT 0,
            FOREIGN KEY (conducteur_id) REFERENCES utilisateurs (id)
        )
        """)

        # Table des réservations
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            utilisateur_id INT NOT NULL,
            trajet_id INT NOT NULL,
            etat VARCHAR(50) DEFAULT 'en attente',
            FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs (id),
            FOREIGN KEY (trajet_id) REFERENCES trajets (id)
        )
        """)

        self.conn.commit()
        print("Tables créées avec succès !")

    def fermer_connexion(self):
        """Ferme la connexion à la base de données."""
        if self.conn:
            self.conn.close()
            print("Connexion fermée.")

    def ajouter_trajet(self, conducteur_id, depart, arrivee, date_heure, prix, places_disponibles):
        """Ajoute un trajet dans la base de données."""
        try:
            query = """
            INSERT INTO trajets (conducteur_id, depart, arrivee, date_heure, prix, places_disponibles)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (conducteur_id, depart, arrivee, date_heure, prix, places_disponibles))
            self.conn.commit()
            print("Trajet ajouté avec succès !")
        except Exception as e:
            print(f"Erreur lors de l'ajout du trajet : {e}")

    def afficher_trajets(self, depart=None, arrivee=None, date=None):
        """Affiche les trajets disponibles en fonction des critères."""
        query = "SELECT * FROM trajets WHERE 1=1"
        params = []

        # Ajouter des filtres si spécifiés
        if depart:
            query += " AND depart = %s"
            params.append(depart)
        if arrivee:
            query += " AND arrivee = %s"
            params.append(arrivee)
        if date:
            query += " AND DATE(date_heure) = %s"
            params.append(date)

        self.cursor.execute(query, params)
        trajets = self.cursor.fetchall()

        print("Trajets disponibles :")
        for trajet in trajets:
            print(trajet)
