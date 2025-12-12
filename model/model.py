import math
import pymunk
from PyQt6.QtCore import pyqtSignal, QThread, QObject, Qt

"""
                          Truc a faire

 1- gravité universelle (gravité en fonction le l'attraction des corps) 
 2- gestion des collisions
 3- play/pause/stop/restart
 4- ajout d'un object   
 5- fix le lag

 """
class Thread(QThread):
    etat = pyqtSignal(bool)

    def run(self):
        self.etat.emit(True)




class Planet(pymunk.Body):
    radius:float
    mass:float
    color:Qt.GlobalColor

    def __init__(self,mass, circle, radius, color):
        super().__init__(mass, circle)

        self.radius = radius
        self.color = color




class Simulation_model(QObject):
    planets = []
    model_changed = pyqtSignal(bool)
    running = False

    def __init__(self):
        super().__init__()
        self.create_sim()

    def create_sim(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.default_planets()
        self.simuler()

        self.model_changed.emit(True)

    def default_planets(self):
        self.add_planet()
        self.add_planet(120, 0, 0, 60, 20, 10, "rouge")

    def add_planet(self, x = 500, y = 20, vx = 10, vy = 10, masse = 10, rayon = 12, couleur = "bleu"):
        body = Planet(masse, pymunk.moment_for_circle(masse, 0, rayon), rayon, couleur)
        body.position = (x, y)
        body.velocity = (vx, vy)

        shape = pymunk.Circle(body, rayon)
        shape.color = couleur

        self.space.add(body, shape)
        self.planets.append(body)

        self.model_changed.emit(True)

    def step(self, dt):
        G = 2000
        n = len(self.planets)
        for i in range(n):
            for j in range(i+1,n):
                p1 = self.planets[i]
                p2 = self.planets[j]


                dx = p2.position.x - p1.position.x
                dy = p2.position.y - p1.position.y
                dist_sqrt = dx * dx + dy * dy

                if dist_sqrt == 0:
                    continue

                dist = math.sqrt(dist_sqrt)
                force_grav = G * p1.mass * p2.mass/ dist_sqrt

                fx = force_grav * dx / dist
                fy = force_grav * dy / dist

                p1.apply_force_at_local_point((fx, fy))
                p2.apply_force_at_local_point((-fx, -fy))

        self.model_changed.emit(True)
        self.space.step(dt)

    def reset_model(self):
        self.__init__()

    def simuler(self):
        running = True
        self.simulation = Thread()
        self.simulation.etat.connect(self.etat)
        self.simulation.finished.connect(self.reset_model)
        self.simulation.start()      # le thread fait lag l'app
        pass

    def etat(self, etat):
        if etat == False:
            pass
            #pause sim/ show pause text
        else:
            self.step(1/60)

    def play_simulation(self):
        print("play")

    def pause_simulation(self):
        print("pause")

    def stop_simulation(self):
        print("stop")