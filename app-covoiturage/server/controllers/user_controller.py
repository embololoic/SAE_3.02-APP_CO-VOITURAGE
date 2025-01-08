from server.models.utilisateur import UtilisateurModel

class UserController:
    def __init__(self, db):
        self.utilisateur_model = UtilisateurModel(db)

    def login(self, data):
        """Gère la connexion d'un utilisateur."""
        email = data.get("email")
        mot_de_passe = data.get("mot_de_passe")
        utilisateur = self.utilisateur_model.verifier_identifiants(email, mot_de_passe)
        if utilisateur:
            return {"status": "success", "message": "Connexion réussie", "data": utilisateur}
        else:
            return {"status": "error", "message": "Identifiants incorrects"}

    def register(self, data):
        """Gère l'inscription d'un utilisateur."""
        try:
            self.utilisateur_model.ajouter_utilisateur(
                data["nom"], data["prenom"], data["email"], data["mot_de_passe"]
            )
            return {"status": "success", "message": "Inscription réussie"}
        except Exception as e:
            return {"status": "error", "message": f"Erreur lors de l'inscription : {e}"}
