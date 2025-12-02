import sys
import traceback

from PyQt6.QtWidgets import QApplication

from view import view
from model import model
from controller import controller


def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

if __name__ == "__main__":
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)

    view = view.View()
    model = model.Model()
    controller = controller.Controller()

    view.show()
    sys.exit(app.exec())

