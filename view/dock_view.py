from PyQt6.QtWidgets import QDockWidget, QPushButton
from PyQt6.uic import loadUi

class dock_view(QDockWidget):


    def __init__(self, nom, parent):
        super().__init__(nom,parent)

        loadUi("ui/dockAdd.ui", self)

