import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server')))
from server.models.trajet import TrajetModel
import logging
import datetime

logging.basicConfig(level=logging.INFO)

def add_trajet(data,conn):
    """
    Handles the addition of a new trip.

    Args:
        data (dict): Trip data, including:
            - conducteur_id (driver's ID)
            - depart (departure location)
            - arrivee (arrival location)
            - date_heure (date and time)
            - prix (price)
            - places_disponibles (available seats)

    Returns:
        dict: A response indicating the success or failure of the operation.
    """
    try:
        # Journaliser les données d'entrée
        logging.info(f"Ajout du trajet avec les données : {data}")

        # Création d'une instance de modèle de trajet
        trajet_model = TrajetModel(conn)
        trajet_id = trajet_model.create_trajet(data)
        # Enregistrement du succès de la création
        logging.info(f"Trajet créé avec succès avec l'ID : {trajet_id}")

        return {"status": "success", "trajet_id": trajet_id}
    except Exception as e:
        # Journaliser l'erreur en cas d'échec
        logging.info(f"Erreur lors de l'ajout du trajet : {e}")

        return {"status": "error", "message": str(e)}

def list_trajets(conn):
    """
    Récupère tous les trajets disponibles depuis la base de données.

    Args:
        conn: Connexion à la base de données.

    Returns:
        dict: Liste des trajets ou message d'erreur.
    """
    try:
        trajet_model = TrajetModel(conn)
        trajets = trajet_model.get_all_trajets()

        # Convertir les objets datetime en chaînes de caractères
        for trajet in trajets:
            if isinstance(trajet["date_heure"], datetime.datetime):
                trajet["date_heure"] = trajet["date_heure"].strftime('%Y-%m-%d %H:%M:%S')

        return {"status": "success", "trajets": trajets}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def search_trajets(filters):
    """
    Searches for trips based on specific criteria.

    Args:
        filters (dict): Search criteria, including:
            - depart (optional)
            - arrivee (optional)
            - date_heure (optional)

    Returns:
        dict: A response containing matching trips or an error.
    """
    try:
        # Appliquer les filtres de recherche
        trajet_model = TrajetModel()
        trajets = trajet_model.search_trajets(filters)
        if trajets:
            return {"status": "success", "trajets": trajets}
        else:
            # Aucun trajet trouvé pour les critères spécifiés
            return {"status": "error", "message": "Aucun trajet trouvé pour les critères spécifiés."}
    except Exception as e:
        # Gérer les exceptions et retourner une erreur
        return {"status": "error", "message": str(e)}

def delete_trajet(trajet_id,conn):
    """
    Deletes a trip by its ID.

    Args:
        trajet_id (int): The ID of the trip to be deleted.

    Returns:
        dict: A response indicating the success or failure of the operation.
    """
    try:
        # Suppression du trajet basé sur l'ID
        trajet_model = TrajetModel(conn)
        success = trajet_model.delete_trajet(trajet_id)
        if success:
            return {"status": "success", "message": "Trajet supprimé avec succès."}
        else:
            # Échec de la suppression
            return {"status": "error", "message": "Erreur lors de la suppression du trajet."}
    except Exception as e:
        # Gérer les exceptions et retourner une erreur
        return {"status": "error", "message": str(e)}
