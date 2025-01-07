import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from modele.database_sql import BaseDonnees

def initialiser_base():
    # Créer une instance de la base de données
    db = BaseDonnees()

    # Créer les tables
    try:
        print("Création des tables...")
        db.creer_tables()

        # Jeu d'insertion
        print("Insertion de données de test...")
        db.cursor.execute("""
        INSERT INTO utilisateurs (
            nom, prenom, email, mot_de_passe, adresse, coordonnees_gps,
            places_voiture, cv_fiscaux, indisponibilites, emploi_du_temps, role
        ) VALUES
            ('Dupont', 'Jean', 'jean.dupont@example.com', 'password123', '123 rue de Paris', '48.8566,2.3522', 4, 6, 'Lundi,Mardi', NULL, 'user'),
            ('Durand', 'Marie', 'marie.durand@example.com', 'password456', '456 rue de Lyon', '45.7640,4.8357', 2, 4, 'Mercredi,Vendredi', NULL, 'admin')
        """)

        db.cursor.execute("""
        INSERT INTO trajets (
            conducteur_id, depart, arrivee, date_heure, prix, places_disponibles, distance_km, impact_carbone, cout_total
        ) VALUES
            (1, 'Paris', 'Lyon', '2025-01-15 08:00:00', 30.0, 2, 465.0, 27900.0, 232.5),
            (2, 'Lyon', 'Marseille', '2025-01-16 14:00:00', 25.0, 1, 315.0, 18900.0, 157.5)
        """)

        db.cursor.execute("""
        INSERT INTO reservations (
            utilisateur_id, trajet_id, etat
        ) VALUES
            (1, 1, 'confirmée'),
            (2, 2, 'en attente')
        """)

        db.conn.commit()
        print("Données de test insérées avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la base : {e}")
    finally:
        db.fermer_connexion()

if __name__ == "__main__":
    initialiser_base()
