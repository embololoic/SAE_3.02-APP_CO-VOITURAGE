import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import socket
import json
import struct
from server.controllers.trajet_controller import add_trajet, delete_trajet, list_trajets, search_trajets
from server.controllers.user_controller import UserController
import MySQLdb

def handle_client(client_socket, user_controller, db_connection):
    """
    Handle a client request and route it to the appropriate controller.

    Args:
        client_socket: The client socket.
        user_controller: UserController instance for managing user actions.
        db_connection: The database connection.
    """
    try:
        # Receive data from the client
        data = client_socket.recv(14096).decode('utf-8')
        request = json.loads(data)
        print(f"Données reçues : {data}")

        # Determine the action and its associated data
        action = request.get("action")
        request_data = request.get("data", {})
        print(f"Action à effectuer : {action}")

        # Route the request to the appropriate controller
        if action == "add_trajet":
            response = add_trajet(request_data, db_connection)  # Passer la connexion ici
        elif action == "delete_trajet":
            response = delete_trajet(request_data.get("trajet_id"), db_connection)
        elif action == "list_trajets":
            response = list_trajets(db_connection)
        elif action == "search_trajets":
            response = search_trajets(request_data, db_connection)
        elif action == "login":
            response = user_controller.login_user(request_data)
        elif action == "register":
            response = user_controller.register_user(request_data)
        else:
            response = {"status": "error", "message": "Action inconnue"}

        # Send the response back to the client
        print(f"Réponse : {response}")
        client_socket.send(json.dumps(response).encode('utf-8'))
    except Exception as e:
        error_message = {"status": "error", "message": str(e)}
        print(f"Erreur : {error_message}")
        client_socket.send(json.dumps(error_message).encode('utf-8'))
    finally:
        # Close the client socket
        client_socket.close()

def start_server(host="127.0.0.1", port=12345):
    """
    Start the server and listen for incoming client connections.

    Args:
        host: The server's host address (default: 127.0.0.1).
        port: The port on which the server listens (default: 12345).
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    l_onoff = 1
    l_linger = 0
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Serveur à l'écoute sur {host}:{port}")

    try:
        # Connect to the database
        db_connection = MySQLdb.connect(user='root', passwd='', db='covoiturage', host='localhost')
        user_controller = UserController(db_connection)
        print("Connexion à la base de données réussie.")
    except MySQLdb.Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return

    try:
        while True:
            # Accept client connections
            client_socket, addr = server_socket.accept()
            print(f"Connexion reçue de {addr}")
            handle_client(client_socket, user_controller, db_connection)  # Passer la connexion ici
    except KeyboardInterrupt:
        print("Arrêt du serveur demandé par l'utilisateur.")
    finally:
        # Clean up resources
        server_socket.close()
        db_connection.close()
        print("Serveur arrêté proprement.")

if __name__ == "__main__":
    start_server()
