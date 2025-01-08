from client.utils.protocol import ClientProtocol

class RegisterController:
    def __init__(self):
        self.client = ClientProtocol()

    def enregistrer_utilisateur(self, data):
        """Simule une requête simple pour tester la connexion."""
        try:
            response = self.client.envoyer_requete("test", {"message": "ping"})
            print(f"Réponse du serveur : {response}")
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")
