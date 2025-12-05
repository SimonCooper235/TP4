import pymunk

"""
            Truc a faire / fonctionalité requise

 1- gravité universelle (gravité en fonction le l'attraction des corps)
 2- gestion des collisions
 3- play/pause/stop/restart
 4- ajout d'un object
 
 """


class Planete():
    mass:int
    radius:int

    def __init__(self, mass, radius):
        super().__init__()



    def temp(self):
        self.body = pymunk.Body(self.mass, pymunk.moment_for_circle(self.mass,0,self.radius))


class Simulation_model():

    objects:[] #  --> liste de planetes

    def __init__(self):
#       super().__init__()
        self.simulation()


    def simulation(self):

        # déclaration de l'espace pymunk et de la liste d'object simulé
        self.space = pymunk.Space()
        self.objects = []

        #  ajout manuel temporaire --> remplacer par ajout_object()
        self.body = pymunk.Body(2, pymunk.moment_for_circle(2,0,2))
        self.space.add(self.body)
        self.objects.append(self.body)


    def update_Simulation(self):
        dt = 1/60

        self.space.step(dt)
        self.__controller.update_view() #  --> ajoute l'info requise pour la view


    def ajout_object(self, object:Planete, pos):  #  --> gestion de la position et de l'impulsion
        self.space.add(object)
        self.objects.append(object)

    def retirer_object(self):
        # retirer l'object de l'espace pymunk et de la liste d'object
        pass

    def edit_object(self, object_to_modifiy:Planete, new_object:Planete):
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

