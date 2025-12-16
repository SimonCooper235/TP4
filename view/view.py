from typing import TYPE_CHECKING
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.uic import loadUi

from view.dock_view import Dock_view

if TYPE_CHECKING:
    from controller.controller import Simulation_controller


class Simulation_view(QMainWindow):
    __dock:Dock_view

    def __init__(self):
        super().__init__()

        loadUi("ui/v1.ui", self)

        self.__dock = Dock_view("Dock", self)
        self.__dock.show()

        if TYPE_CHECKING:
            self.__controller: Simulation_controller | None = None


    def set_Controller(self, c):
        self.__controller = c

    def get_dock(self):
        return self.__dock

    def ajout_object(self, object):
        self.__controller.ajout_object(object)

    def paintEvent(self, event):
       planets = self.__controller.get_planets()

       p = QPainter(self)
       p.fillRect(self.rect(), Qt.GlobalColor.black)

       for i in range(len(planets)):
           p.setBrush(Qt.GlobalColor.cyan)
           planet = planets[i]
           x, y = planet.position
           # p.setBrush(planet.color)
           p.setBrush(Qt.GlobalColor.cyan)

           x, y = planet.position
           p.drawEllipse(
               int(400 - x),
               int(250 - y),
               2 * int(self.__controller.get_rad(i)),
               2 * int(self.__controller.get_rad(i))
           )

       self.update()