import sys
import traceback

from PyQt6.QtWidgets import QApplication

from view.view import Simulation_view
from model.model import Simulation_model
from controller.controller import Simulation_controller

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

if __name__ == "__main__":
    sys.excepthook = qt_exception_hook

    app = QApplication(sys.argv)

    view = Simulation_view()
    model = Simulation_model()
    controler = Simulation_controller(model, view)

    window = view
    window.show()

    sys.exit(app.exec())

