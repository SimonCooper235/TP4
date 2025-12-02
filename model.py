import pymunk



class Simulation_model():

    def __init__(self):
        pass


    def simulation(self):

        self.space = pymunk.space()


    def set_controller(self, controller):
        self.__controller = controller