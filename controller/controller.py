from PyQt6.QtCore import QTimer

from model import model
from view import view


class Simulation_controller():
    __model:model.Simulation_model
    __view:view.Simulation_view


    def __init__(self, model, view):
        self.__model = model
        self.__view = view
        self.__view.set_Controller(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.running = False

        self.__view.play_pushButton.clicked.connect(self.play)
        self.__view.pause_pushButton.clicked.connect(self.pause)
        self.__view.stop_pushButton.clicked.connect(self.stop)

        self.__view.get_dock().createPushButton.clicked.connect(self.ajout_object)

    def ajout_object(self):
        self.__model.add_planet(int(self.__view.get_dock().posXLineEdit.text()),
                                int(self.__view.get_dock().posYLineEdit.text()),
                                int(self.__view.get_dock().masseLineEdit.text()),
                                int(self.__view.get_dock().radiusLineEdit.text())
                                )

    def play(self):
        if not self.running:
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
        self.__model.step(1 / 60)
        self.__view.update()

    def get_planets(self):
        return self.__model.planets

    def get_rad(self, i):
        return self.__model.get_rad(i)
