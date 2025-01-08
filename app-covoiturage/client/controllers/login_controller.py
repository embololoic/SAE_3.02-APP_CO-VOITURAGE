from client.utils.protocol import ClientProtocol

class LoginController:
    def __init__(self):
        self.client = ClientProtocol()

    def verifier_identifiants(self, email, mot_de_passe):
        """Envoie les identifiants au serveur pour vérification."""
        return self.client.envoyer_requete("login", {"email": email, "mot_de_passe": mot_de_passe})
