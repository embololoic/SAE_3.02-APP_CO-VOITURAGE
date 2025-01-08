class UtilisateurModel:
    def __init__(self, db):
        self.db = db

    def verifier_identifiants(self, email, mot_de_passe):
        query = "SELECT * FROM utilisateurs WHERE email = %s AND mot_de_passe = %s"
        self.db.cursor.execute(query, (email, mot_de_passe))
        return self.db.cursor.fetchone()

    def ajouter_utilisateur(self, nom, prenom, email, mot_de_passe, role="user"):
        query = """
            INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.db.cursor.execute(query, (nom, prenom, email, mot_de_passe, role))
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return False
