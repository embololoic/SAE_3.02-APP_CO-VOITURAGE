CREATE Table utilisateur(
id SERIAL PRIMARY KEY,
nom VARCHAR (30) NOT NULL,
prenom VARCHAR (30) NOT NULL,
login VARCHAR (30) UNIQUE NOT NULL,
password CHAR(128) NOT NULL,
adresse VARCHAR(100) NOT NULL,
coordonnees_gps Float,
telephone VARCHAR(15),
nombre_places_voiture INT DEFAULT 0,
nombre_cv_fiscaux INT,
jours_indisponibilite DATE,
cout_cumule NUMERIC(10, 2) DEFAULT 0 NOT NULL,
bilan_carbone NUMERIC(10, 2) DEFAULT 0 NOT NULL
);