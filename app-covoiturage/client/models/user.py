# client/models/user.py
class User:
    def __init__(self, nom, prenom, login, password, adresse, gps, telephone, edt, places, cv_fiscaux,
                 indisponibilites):
        self.nom = nom
        self.prenom = prenom
        self.login = login
        self.password = password  # Haché avant stockage pour la sécurité
        self.adresse = adresse
        self.gps = gps
        self.telephone = telephone
        self.edt = edt
        self.places = places
        self.cv_fiscaux = cv_fiscaux
        self.indisponibilites = indisponibilites
        self.cout_cumule = 0
        self.bilan_carbone = 0

    def calculer_cout_trajet(self, distance):
        # Exemple de calcul (à adapter selon règles fiscales)
        self.cout_cumule += distance * 0.15

    def calculer_bilan_carbone(self, distance):
        # Exemple de calcul de bilan carbone (à affiner)
        self.bilan_carbone += distance * 0.1
