import socket
import json

class ServeurCovoiturage:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port

    def demarrer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
            serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Réutilisation du port
            serveur.bind((self.host, self.port))
            serveur.listen(5)
            print(f"Serveur démarré sur {self.host}:{self.port}")

            while True:
                client_socket, client_address = serveur.accept()
                print(f"Connexion reçue de {client_address}")
                self.gestion_client(client_socket)

    def gestion_client(self, client_socket):
        try:
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Données reçues du client : {data}")
            import json
            try:
                print("Test de sérialisation JSON...")
                json.dumps(data)
                print("Les données sont sérialisables.")
            except Exception as e:
                print(f"Erreur de sérialisation JSON : {e}")
                return {"status": "error", "message": "Données invalides"}
            print(f"Taille des données JSON : {len(json.dumps(data).encode('utf-8'))} octets")

            if data:
                requete = json.loads(data)
                action = requete.get("action")
                print(f"Action demandée : {action}")

                if action == "register":
                    # Exemple de réponse simulée pour tester
                    reponse = {"status": "success", "message": "Utilisateur enregistré"}
                    client_socket.send(json.dumps(reponse).encode('utf-8'))
                elif action == "test":
                    reponse = {"status": "success", "message": "pong"}
                    client_socket.send(json.dumps(reponse).encode('utf-8'))

                else:
                    reponse = {"status": "error", "message": "Action inconnue"}


                print(f"Réponse au client : {reponse}")
                client_socket.send(json.dumps(reponse).encode('utf-8'))
        except Exception as e:
            print(f"Erreur dans la gestion du client : {e}")
        finally:
            client_socket.close()


if __name__ == "__main__":
    serveur = ServeurCovoiturage()
    serveur.demarrer()
