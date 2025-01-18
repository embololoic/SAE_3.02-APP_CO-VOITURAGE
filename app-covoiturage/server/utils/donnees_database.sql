INSERT INTO trajets (conducteur_id, depart, arrivee, date_heure, prix, places_disponibles, distance_km, impact_carbone, cout_total, description, etat) VALUES
(1, 'Paris', 'Lyon', '2025-01-15 10:00:00', 30.0, 4, 465.0, 50.0, 100.0, 'Trajet rapide et confortable', 'en attente'),
(2, 'Marseille', 'Nice', '2025-02-20 14:00:00', 25.0, 3, 200.0, 30.0, 80.0, 'Trajet avec vue sur la mer', 'en attente'),
(3, 'Bordeaux', 'Toulouse', '2025-03-10 08:00:00', 20.0, 5, 250.0, 40.0, 90.0, 'Trajet agréable', 'en attente'),
(4, 'Lille', 'Bruxelles', '2025-04-05 12:00:00', 15.0, 2, 110.0, 20.0, 50.0, 'Trajet international', 'en attente'),
(5, 'Nantes', 'Rennes', '2025-05-18 09:00:00', 10.0, 6, 100.0, 10.0, 30.0, 'Trajet court', 'en attente');

-- Inserting multiple records into the utilisateurs table
INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, adresse, coordonnees_gps, places_voiture, cv_fiscaux, indisponibilites, emploi_du_temps, role) VALUES
('Dupont', 'Jean', 'jean.dupont@example.com', 'password123', '123 Rue de Paris, Paris', '48.8566,2.3522', 4, 5, 'Lundi, Mardi', '8h-18h', 'user'),
('Martin', 'Sophie', 'sophie.martin@example.com', 'password456', '456 Avenue de Lyon, Lyon', '45.7640,4.8357', 3, 4, 'Mercredi, Jeudi', '9h-17h', 'user'),
('Durand', 'Pierre', 'pierre.durand@example.com', 'password789', '789 Boulevard de Marseille, Marseille', '43.2965,5.3698', 2, 3, 'Vendredi', '10h-16h', 'user'),
('Petit', 'Marie', 'marie.petit@example.com', 'password101', '101 Rue de Bordeaux, Bordeaux', '44.8378,-0.5792', 5, 6, 'Samedi, Dimanche', '11h-15h', 'user'),
('Leroy', 'Luc', 'luc.leroy@example.com', 'password202', '202 Rue de Lille, Lille', '50.6292,3.0573', 4, 5, 'Lundi, Mardi', '12h-14h', 'admin');

-- Inserting multiple records into the reservations table
INSERT INTO reservations (utilisateur_id, trajet_id, etat, date_reservation) VALUES
(1, 1, 'en attente', '2025-01-01 10:00:00'),
(2, 2, 'en attente', '2025-02-01 11:00:00'),
(3, 3, 'en attente', '2025-03-01 12:00:00'),
(4, 4, 'en attente', '2025-04-01 13:00:00'),
(5, 5, 'en attente', '2025-05-01 14:00:00');
