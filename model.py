import pymunk



class Simulation_model():

    objects:[]

    def __init__(self):
        self.objects = []

        self.simulation()


    def simulation(self):
        self.space = pymunk.Space()
        # ajout d'une gravité



        self.body = pymunk.Body(2, pymunk.moment_for_circle(2,0,2))
        self.space.add(self.body)

        self.objects.append(self.body)
        print(self.objects)

    def update_Simulation(self):
        dt = 1/60

        self.space.step(dt)
        # update le visuel de la vue

    def ajout_object(self, object:pymunk.Body):
        self.space.add(object)
        self.objects.append(object)

    def retirer_object(self):
        # retirer l'object de l'espace pymunk et de la liste d'object
        pass

    def edit_object(self, object_to_modifiy:pymunk.Body, new_object:pymunk.Body):
        # retirer l'object de l'espace pymunk et de la liste d'object puis le remplacer par le nouvel object
        pass

    def pause_Simulation(self):
        pass

    def play_Simulation(self):
        pass

    def stop_Simulation(self):
        pass



    def set_controller(self, controller):
        self.__controller = controller