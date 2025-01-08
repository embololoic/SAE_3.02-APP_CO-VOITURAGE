class Utilisateur:
    def __init__(self, nom, prenom, email, mot_de_passe, role="user"):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.role = role

    def to_dict(self):
        """Convertit l'utilisateur en dictionnaire pour l'envoi au serveur."""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "mot_de_passe": self.mot_de_passe,
            "role": self.role,
        }
