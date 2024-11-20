# client/models/user.py
import bcrypt

class User:
    def __init__(self, nom, prenom, login, password, adresse, gps, telephone, edt, places, cv_fiscaux, indisponibilites):
        self.nom = nom
        self.prenom = prenom
        self.login = login
        self.password = self.hash_password(password)  # Hachage du mot de passe pour la sécurité
        self.adresse = adresse
        self.gps = gps
        self.telephone = telephone
        self.edt = edt
        self.places = int(places)
        self.cv_fiscaux = int(cv_fiscaux)
        self.indisponibilites = indisponibilites
        self.cout_cumule = 0
        self.bilan_carbone = 0

    def hash_password(self, password):
        """Hache le mot de passe avec bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        """Vérifie le mot de passe"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def calculer_cout_trajet(self, distance):
        """Calculer le coût du trajet selon la distance"""
        self.cout_cumule += distance * 0.15  # Exemple de coût par km
        return self.cout_cumule

    def calculer_bilan_carbone(self, distance):
        """Calculer le bilan carbone selon la distance"""
        self.bilan_carbone += distance * 0.1  # Exemple de CO2 par km
        return self.bilan_carbone

    def __repr__(self):
        return f"User({self.nom}, {self.prenom}, {self.login}, {self.adresse})"

# client/models/user_model.py


class UserModel:
    def __init__(self):
        self.users = []  # Liste temporaire des utilisateurs (peut être remplacée par une base de données)

    def create_user(self, user_data):
        """Créer un utilisateur et l'ajouter à la liste"""
        user = User(**user_data)  # Création de l'instance User avec les données fournies
        self.users.append(user)
        print(f"Utilisateur {user.nom} {user.prenom} enregistré avec succès!")
        return user

    def get_user_by_login(self, login):
        """Récupérer un utilisateur par son login"""
        for user in self.users:
            if user.login == login:
                return user
        return None  # Si aucun utilisateur n'est trouvé

    def delete_user(self, login):
        """Supprimer un utilisateur par son login"""
        user = self.get_user_by_login(login)
        if user:
            self.users.remove(user)
            print(f"Utilisateur {user.nom} {user.prenom} supprimé.")
            return True
        return False

    def update_user(self, login, updated_data):
        """Mettre à jour les informations d'un utilisateur"""
        user = self.get_user_by_login(login)
        if user:
            for key, value in updated_data.items():
                setattr(user, key, value)  # Mettre à jour chaque attribut de l'utilisateur
            print(f"Utilisateur {user.nom} {user.prenom} mis à jour avec succès.")
            return user
        return None
