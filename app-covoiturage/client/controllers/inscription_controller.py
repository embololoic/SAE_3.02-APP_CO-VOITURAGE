# client/controllers/inscription_controller.py
class InscriptionController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self  # Assigne le contrôleur à la vue

    def create_account(self):
        # Récupération des données depuis la vue
        user_data = {
            "nom": self.view.nom.text(),
            "prenom": self.view.prenom.text(),
            "login": self.view.login.text(),
            "password": self.view.password.text(),  # A hacher avant envoi
            "adresse": self.view.adresse.text(),
            "telephone": self.view.telephone.text(),
            "edt": self.view.edt.text(),
            "places": self.view.places.text(),
            "cv_fiscaux": self.view.cv_fiscaux.text(),
            "indisponibilites": self.view.indisponibilites.text(),
        }
        # Ici, on appellerait le serveur pour enregistrer l'utilisateur
        # Exemple de connexion serveur non incluse ici pour simplification
