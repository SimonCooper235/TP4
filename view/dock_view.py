from PyQt6.QtWidgets import QDockWidget, QPushButton, QLineEdit, QComboBox
from PyQt6.uic import loadUi

class Dock_view(QDockWidget):
    masseLineEdit : QLineEdit
    radiusLineEdit : QLineEdit
    posXLineEdit : QLineEdit
    posYLineEdit : QLineEdit
    couleurComboBox : QComboBox
    createPushButton : QPushButton


    def __init__(self, nom, parent):
        super().__init__(nom,parent)

        loadUi("ui/dockAdd.ui", self)

