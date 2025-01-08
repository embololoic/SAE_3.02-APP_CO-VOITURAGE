class Validation:
    @staticmethod
    def champs_remplis(**kwargs):
        """Vérifie que tous les champs obligatoires sont remplis."""
        for champ, valeur in kwargs.items():
            if champ not in ["gps", "emploi_du_temps"] and not valeur.strip():
                return False, f"Le champ '{champ}' est obligatoire."
        return True, "OK"
