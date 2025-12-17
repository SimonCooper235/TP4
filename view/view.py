from typing import TYPE_CHECKING
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QHBoxLayout
from PyQt6.uic import loadUi

from view.dock_view import Dock_view
from view.graphe_view import Graphe_view

if TYPE_CHECKING:
    from controller.controller import Simulation_controller


class Simulation_view(QMainWindow):
    __dock:Dock_view
    __graphe : Graphe_view

    playPushButton : QPushButton
    pausePushButton : QPushButton
    stopPushButton : QPushButton

    def __init__(self):
        super().__init__()

        loadUi("ui/v1.ui", self)

        self.__dock = Dock_view("Dock", self)
        self.__graph = Graphe_view()

        self.__graph.show()

        if TYPE_CHECKING:
            self.__controller: Simulation_controller | None = None


    def set_Controller(self, c):
        self.__controller = c

    def get_dock(self):
        return self.__dock

    def get_graph(self):
        return self.__graph

    def ajout_object(self, object):
        self.__controller.ajout_object(object)

    def paintEvent(self, event):
       planets = self.__controller.get_planets()

       p = QPainter(self)
       #p.fillRect(self.rect(), Qt.GlobalColor.black)

       for i in range(len(planets)):
           planet = planets[i]
           x, y = planet.position

           color = self.__controller.get_couleurs(i)
           p.setBrush(QColor(color))

           x, y = planet.position
           r = int(self.__controller.get_rad(i))
           p.drawEllipse(
               int(400 - x),
               int(250 - y),
               2 * r,
               2 * r
           )
    def keyPressEvent(self, event):
        if event.key() == 80:
            self.__controller.p_pressed()
        elif event.key() == 16777216:
            self.__controller.esc_pressed()
        elif event.key() == 71:
            self.__controller.g_pressed()