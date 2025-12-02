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


