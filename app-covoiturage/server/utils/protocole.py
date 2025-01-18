import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
import socket
import json
import struct
from server.controllers.trajet_controller import add_trajet, delete_trajet, list_trajets, search_trajets
from server.controllers.user_controller import UserController
import MySQLdb

def handle_client(client_socket, user_controller):
    try:
        data = client_socket.recv(4096).decode('utf-8')
        request = json.loads(data)
        print(f"Données reçues : {data}")

        action = request.get("action")
        data = request.get("data", {})
        print(f"Action à effectuer : {action}")

        if action == "add_trajet":
            response = add_trajet(data)
        elif action == "delete_trajet":
            response = delete_trajet(data)
        elif action == "list_trajets":
            response = list_trajets()
        elif action == "search_trajets":
            response = search_trajets(data)
        elif action == "login":
            response = user_controller.login_user(data)
        elif action == "register":
            response = user_controller.register_user(data)
        else:
            response = {"status": "error", "message": "Action inconnue"}

        print(f"Réponse : {response}")
        client_socket.send(json.dumps(response).encode('utf-8'))
    except Exception as e:
        client_socket.send(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        print(f"Erreur : {e}")
    finally:
        client_socket.close()

def start_server(host="172.17.21.21", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    l_onoff = 1
    l_linger = 0
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Serveur à l'écoute sur {host}:{port}")

    try:
        db_connection = MySQLdb.connect(user='rsissako', passwd='Fatou7151@', db='rsissako1', host='192.168.156.221')
        user_controller = UserController(db_connection)
        print("Connexion à la base de données réussie.")
    except MySQLdb.Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connexion reçue de {addr}")
            handle_client(client_socket, user_controller)
    except KeyboardInterrupt:
        print("Arrêt du serveur demandé par l'utilisateur.")
    finally:
        server_socket.close()
        db_connection.close()
        print("Serveur arrêté proprement.")

if __name__ == "__main__":
    start_server()
