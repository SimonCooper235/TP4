import model
import view


class Simulation_controler():
    __model:model.Simulation_model
    __view:view.Simulation_view


    def __init__(self, model, view):
        self.__view=view
        self.__view.set_controller(self)

        self.__model=model
        self.__model.set_controller(self)

    def ajout_object(self, object):
        self.__model.ajout_object(object)

    def update_view(self):
        self.__view.paintEvent()

    def play(self):
        self.__model.play_Simulation()

    def pause(self):
        self.__model.pause_Simulation()

    def stop(self):
        self.__model.stop_Simulation()
