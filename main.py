import sys
from PyQt6.QtWidgets import QApplication, QWidget

import view
import model
import controler

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = view.Simulation_view()
    model = model.Simulation_model()
    controler = controler.Simulation_controler(model, view)

    window = view
    window.show()

    sys.exit(app.exec())

