import sys
import traceback

from PyQt6.QtWidgets import QApplication, QWidget

from view import Simulation_view
from model import Simulation_model
from controler import Simulation_controler

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

if __name__ == "__main__":
    sys.excepthook = qt_exception_hook

    app = QApplication(sys.argv)

    view = Simulation_view()
    model = Simulation_model()
    controler = Simulation_controler(model, view)

    window = view
    window.show()

    sys.exit(app.exec())

