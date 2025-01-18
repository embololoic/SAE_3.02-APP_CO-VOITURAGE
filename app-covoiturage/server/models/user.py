import MySQLdb

class UserModel:
    """
    Model for managing users in the database.
    """

    def __init__(self, conn):
        """
        Initializes the UserModel class.

        Args:
            conn (MySQLdb.Connection): The MySQL database connection.
        """
        # Initialiser la connexion à la base de données
        self.conn = conn

    def create_user(self, user_data):
        """
        Adds a user to the database.

        Args:
            user_data (dict): User data including:
                - nom: Last name.
                - prenom: First name.
                - email: Email address.
                - mot_de_passe: Password.
                -addresse: Address.
                -coordonnees_gps: GPS coordinates.
                -places_voiture: Number of car seats.
                - cv_fiscaux: Number of tax documents.
                - indisponibilite: Days of unavailability.
                - emploi_du_temps: Schedule.

        Returns:
            int: The ID of the added user.
            False: If an error occurs during insertion.
            None: If no user is added.
        """
        try:
            cursor = self.conn.cursor()
            # Requête SQL pour insérer un nouvel utilisateur
            cursor.execute("""
                INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, adresse, coordonnees_gps, places_voiture, cv_fiscaux, indisponibilites, emploi_du_temps)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (user_data["nom"], user_data["prenom"], user_data["email"], user_data["mot_de_passe"], user_data["adresse"], user_data["coordonnees_gps"], user_data["places_voiture"], user_data["cv_fiscaux"], user_data["indisponibilites"], user_data["emploi_du_temps"]))
            self.conn.commit()
            return cursor.lastrowid
        except MySQLdb.IntegrityError as e:
            if e.args[0] == 1062:  # Code MySQL pour un duplicata
                raise ValueError("Cet email est déjà utilisé.")
            raise

    def get_user_by_id(self, user_id):
        """
        Retrieves a user by their ID.

        Args:
            user_id (int): The user's ID.

        Returns:
            dict: User data if found, None otherwise.
        """
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        # Requête SQL pour récupérer un utilisateur par ID
        cursor.execute("SELECT * FROM utilisateurs WHERE id = %s", (user_id,))
        return cursor.fetchone()

    def get_user_by_email(self, email):
        """
        Retrieves a user by their email address.

        Args:
            email (str): The user's email address.

        Returns:
            dict: User data if found, None otherwise.
        """
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        # Requête SQL pour récupérer un utilisateur par email
        cursor.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
        return cursor.fetchone()

    def update_user(self, user_id, data):
        """
        Updates an existing user.

        Args:
            user_id (int): The ID of the user to update.
            data (dict): A dictionary containing the fields to update.

        Returns:
            bool: True if the update is successful, False otherwise.
        """
        try:
            # Générer les champs à mettre à jour dynamiquement
            updates = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE utilisateurs SET {updates} WHERE id = %s"
            cursor = self.conn.cursor()
            # Exécuter la requête de mise à jour
            cursor.execute(query, (*data.values(), user_id))
            self.conn.commit()
            return True
        except MySQLdb.Error as err:
            # Gestion des erreurs SQL
            print(f"Erreur lors de la mise à jour de l'utilisateur : {err}")
            return False

    def delete_user(self, user_id):
        """
        Deletes a user by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the deletion is successful, False otherwise.
        """
        try:
            # Requête SQL pour supprimer un utilisateur par ID
            query = "DELETE FROM utilisateurs WHERE id = %s"
            cursor = self.conn.cursor()
            cursor.execute(query, (user_id,))
            self.conn.commit()
            return True
        except MySQLdb.Error as err:
            # Gestion des erreurs SQL
            print(f"Erreur lors de la suppression de l'utilisateur : {err}")
            return False
