from typing import TYPE_CHECKING

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.uic import loadUi

if TYPE_CHECKING:
    from controller.controller import Simulation_controller


class Simulation_view(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("ui/v1.ui", self) # TODO  faire le ui

        if TYPE_CHECKING:
            self.__controller:Simulation_controller



    def ajout_object(self, object):
        self.__controller.ajout_object(object)

    def paintEvent(self, event):
       pass
