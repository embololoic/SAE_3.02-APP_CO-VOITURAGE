# client/controllers/inscription_controller.py
class InscriptionController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self  # Lien avec la vue

    def handle_submit(self):
        # Récupérer les données de la vue
        user_data = {
            "nom": self.view.nom.text(),
            "prenom": self.view.prenom.text(),
            "login": self.view.login.text(),
            "password": self.view.password.text(),  # À hacher avant envoi au serveur
            "adresse": self.view.adresse.text(),
            "telephone": self.view.telephone.text(),
            "edt": self.view.edt.text(),
            "places": self.view.places.text(),
            "cv_fiscaux": self.view.cv_fiscaux.text(),
            "indisponibilites": self.view.indisponibilites.text(),
        }

        # Appeler le modèle pour enregistrer l'utilisateur
        self.model.create_user(user_data)

    def handle_cancel(self):
        # Réinitialiser ou fermer la fenêtre
        self.view.close()

