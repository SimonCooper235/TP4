from model import model
from view import view


class Simulation_controller():
    __model:model.Simulation_model
    __view:view.Simulation_view


    def __init__(self, model, view):
        self.__model = model
        self.__view = view

        self.__view.play_pushButton.clicked.connect(self.play)
        self.__view.pause_pushButton.clicked.connect(self.pause)
        self.__view.stop_pushButton.clicked.connect(self.stop)

        self.__model.model_changed.connect(self.__view.paintEvent)


    def ajout_object(self, object):
        self.__model.ajout_object(object)

    def play(self):
        self.__model.play_simulation()

    def pause(self):
        self.__model.pause_simulation()

    def stop(self):
        self.__model.stop_simulation()
