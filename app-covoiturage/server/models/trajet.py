import MySQLdb

class TrajetModel:
    """
    Class to manage trips in the database.
    """

    def __init__(self, conn):
        """
        Initializes the connection to the database.

        Args:
            conn (MySQLdb.Connection): The database connection.
        """
        # Initialiser la connexion à la base de données
        self.conn = conn

    def create_trajet(self, trajet_data):
        """
        Creates a new trip in the database.

        Args:
            trajet_data (dict): Data for the new trip, including:
                - conducteur_id: ID of the driver.
                - depart: Departure location.
                - arrivee: Arrival location.
                - date_heure: Date and time of departure.
                - prix: Price of the trip.
                - places_disponibles: Available seats.

        Returns:
            int: ID of the newly created trip.
        """
        cursor = self.conn.cursor()
        # Requête SQL pour insérer un nouveau trajet
        query = """
        INSERT INTO trajets (conducteur_id, depart, arrivee, date_heure, prix, places_disponibles, etat)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            trajet_data["conducteur_id"],
            trajet_data["depart"],
            trajet_data["arrivee"],
            trajet_data["date_heure"],
            trajet_data["prix"],
            trajet_data["places_disponibles"],
            "en attente"  # État initial du trajet
        ))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_trajets(self):
        """
        Retrieves all trips from the database.

        Returns:
            List[dict]: List of trips, each containing:
                - trajet_id (int): Trip ID.
                - conducteur_id (int): Driver ID.
                - depart (str): Departure address.
                - arrivee (str): Arrival address.
                - date_heure (str): Departure date and time.
                - prix (float): Ticket price.
                - places_disponibles (int): Number of available seats.
                - etat (str): Trip status (e.g., "en attente", "en cours", "terminé").
        """
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        # Récupérer tous les trajets depuis la base de données
        cursor.execute("SELECT * FROM trajets")
        return cursor.fetchall()

    def search_trajets(self, filters):
        """
        Searches for trips based on certain filters.

        Args:
            filters (dict): Search criteria, including:
                - depart: Departure location.
                - arrivee: Arrival location.

        Returns:
            List[dict]: List of matching trips.
        """
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        # Requête SQL pour rechercher des trajets en fonction des filtres
        query = "SELECT * FROM trajets WHERE depart = %s AND arrivee = %s"
        cursor.execute(query, (filters["depart"], filters["arrivee"]))
        return cursor.fetchall()

    def delete_trajet(self, trajet_id):
        """
        Deletes a trip by its ID.

        Args:
            trajet_id (int): The ID of the trip to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        try:
            # Requête SQL pour supprimer un trajet par ID
            query = "DELETE FROM trajets WHERE id = %s"
            cursor = self.conn.cursor()
            cursor.execute(query, (trajet_id,))
            self.conn.commit()
            return True
        except MySQLdb.Error as err:
            # Gérer les erreurs SQL
            print(f"Erreur lors de la suppression du trajet : {err}")
            return False
