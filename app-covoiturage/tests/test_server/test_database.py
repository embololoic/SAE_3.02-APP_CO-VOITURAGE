# Tests unitaires pour la classe BaseDonnees
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'server')))
from server.utils.database import BaseDonnees

def test_creation_tables():
    db = BaseDonnees(host="192.168.156.221", user="rsissako", password="Fatou7151@", database="rsissako1")
    try:
        db.creer_tables()
        print("Test réussi : Les tables ont été créées.")
    except Exception as e:
        print(f"Test échoué : {e}")
    finally:
        db.fermer_connexion()

if __name__ == "__main__":
    test_creation_tables()
