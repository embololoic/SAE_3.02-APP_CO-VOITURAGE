import socket
import json

def send_request(action, data):
    client_socket = None
    try:
        # Configuration de la connexion
        host = "172.17.21.21"
        port = 12345
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Préparation de la requête
        request = {
            "action": action,
            "data": data
        }
        client_socket.send(json.dumps(request).encode('utf-8'))

        # Réception de la réponse
        response = client_socket.recv(14024).decode('utf-8')
        return json.loads(response)
    except Exception as e:
        print(f"Erreur lors de la connexion : {e}")
        return {"status": "error", "message": str(e)}
    finally:
        if client_socket:
            client_socket.close()

    return {"status": "error", "message": "Unknown error"}