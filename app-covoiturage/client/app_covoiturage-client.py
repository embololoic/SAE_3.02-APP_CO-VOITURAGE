# client/main.py
import sys
from PyQt5.QtWidgets import QApplication
from models.user_model import UserModel
from controllers.inscription_controller import InscriptionController
from views.inscription_view import InscriptionView

def main():
    app = QApplication(sys.argv)

    # Initialiser le modèle, la vue et le contrôleur
    model = UserModel()
    view = InscriptionView(None)  # Vue sans contrôleur initialement
    controller = InscriptionController(model, view)

    # Afficher la vue
    view.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
