from server.models.user import UserModel

class UserController:
    """
    Controller for managing user-related actions.
    """

    def __init__(self, conn):
        """
        Initializes the controller with a database connection.

        Args:
            conn: Database connection.
        """
        # Initialiser le modèle utilisateur avec la connexion à la base de données
        self.utilisateur_model = UserModel(conn)

    def register_user(self, data):
        """
        Handles user registration.

        Args:
            data (dict): User data, including:
                - nom (last name)
                - prenom (first name)
                - email
                - mot_de_passe (password)
                - adresse (address)
                - coordonnees_gps (GPS coordinates)
                - places_voiture (number of car seats)
                - cv_fiscaux (number of tax documents)
                - indisponibilites (unavailability dates)
                - emploi_du_temps (schedule)

        Returns:
            dict: A response indicating the success or failure of the operation.
        """
        try:
            # Vérifiez si l'email existe déjà
            existing_user = self.utilisateur_model.get_user_by_email(data["email"])
            if existing_user:
                return {"status": "error", "message": "Cet email est déjà utilisé."}

            # Vérification des champs requis
            required_fields = [
                "nom", "prenom", "email", "mot_de_passe", "adresse", "coordonnees_gps", "places_voiture",
                "cv_fiscaux", "indisponibilites", "emploi_du_temps"
            ]
            for field in required_fields:
                if field not in data or not data[field]:
                    # Retourner une erreur si un champ est manquant
                    return {"status": "error", "message": f"Le champ {field} est requis."}

            # Création de l'utilisateur
            user_id = self.utilisateur_model.create_user(data)
            if user_id:
                # Succès de la création
                return {"status": "success", "message": "Utilisateur créé avec succès.", "user_id": user_id}
            else:
                # Échec de la création
                return {"status": "error", "message": "Erreur lors de la création de l'utilisateur."}

        except Exception as e:
            # Gestion des exceptions et journalisation de l'erreur
            return {"status": "error", "message": str(e)}

    def login_user(self, data):
        """
        Handles user login.

        Args:
            data (dict): Login credentials, including:
                - email
                - mot_de_passe (password)

        Returns:
            dict: A response indicating the success or failure of the operation.
        """
        try:
            if "email" not in data or "password" not in data:
                return {"status": "error", "message": "Email et mot de passe requis."}

            user = self.utilisateur_model.get_user_by_email(data["email"])
            if not user:
                return {"status": "error", "message": "Utilisateur introuvable."}

            if user["mot_de_passe"] != data["password"]:
                return {"status": "error", "message": "Mot de passe incorrect."}

            return {"status": "success", "message": "Connexion réussie.", "user": user}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_user(self, user_id):
        """
        Retrieves details of a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            dict: A response containing user information or an error.
        """
        try:
            # Récupérer les informations de l'utilisateur via son ID
            user = self.utilisateur_model.get_user_by_id(user_id)
            if user:
                # Succès de la récupération
                return {"status": "success", "user": user}
            else:
                # Utilisateur introuvable
                return {"status": "error", "message": "Utilisateur introuvable."}

        except Exception as e:
            # Gestion des exceptions et journalisation de l'erreur
            return {"status": "error", "message": str(e)}
