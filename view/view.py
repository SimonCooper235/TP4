from typing import TYPE_CHECKING
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.uic import loadUi

from view.dock_view import dock_view

if TYPE_CHECKING:
    from controller.controller import Simulation_controller


class Simulation_view(QMainWindow):
    __dock:dock_view

    def __init__(self):
        super().__init__()

        loadUi("ui/v1.ui", self)

        self.__dock = dock_view("Dock", self)
        self.__dock.show()

        if TYPE_CHECKING:
            self.__controller:Simulation_controller



    def set_Controller(self, c):
        self.__controller = c

    def get_dock(self):
        return self.__dock

    def ajout_object(self, object):
        self.__controller.ajout_object(object)

    def paintEvent(self, event):
       planets = self.__controller.get_Planets()

       p = QPainter(self)

       for planet in planets:

           #p.setBrush(planet.color)
           p.setBrush(Qt.GlobalColor.cyan)

           x = int(planet.position.x - planet.radius)
           y = int(250 - planet.position.y - planet.radius)

           p.drawEllipse(x,y, 2*planet.radius, 2*planet.radius)

       self.update()