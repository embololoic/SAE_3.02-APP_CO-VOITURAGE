import socket
import json

class ClientProtocol:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port

    def envoyer_requete(self, action, data):
        try:
            print(f"Connexion au serveur {self.host}:{self.port}...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("127.0.0.1", self.port))
                s.connect((self.host, self.port))
                print("Connexion établie. Envoi des données...")
                requete = json.dumps({"action": action, "data": data}).encode("utf-8")
                print(f"Requête JSON prête : {requete}")
                s.sendall(requete)
                print("Données envoyées. Attente de la réponse...")
                reponse = s.recv(1024).decode("utf-8")
                print(f"Réponse reçue du serveur : {reponse}")
                return json.loads(reponse)
        except Exception as e:
            print(f"Erreur dans la connexion ou la communication : {e}")
            return {"status": "error", "message": "Impossible de se connecter au serveur"}
