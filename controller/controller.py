from PyQt6.QtCore import QTimer

from model import model
from view import view


class Simulation_controller():
    __model:model.Simulation_model
    __view:view.Simulation_view


    def __init__(self, model, view):
        self.__model = model
        self.__view = view

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.running = False

        self.__view.play_pushButton.clicked.connect(self.play)
        self.__view.pause_pushButton.clicked.connect(self.pause)
        self.__view.stop_pushButton.clicked.connect(self.stop)


    def ajout_object(self, object):
        self.__model.add_planet(object)

    def play(self):
        if not self.timer.stop():
            self.timer.start(16)
            self.running = True

    def pause(self):
        self.timer.stop()
        self.running = False

    def stop(self):
        self.timer.stop()
        self.running = False
        self.__model.reset()
        self.__view.update()

    def update(self):
        self.__model.step(1/60)
        self.__view.update()