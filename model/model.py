import math

import pymunk
from PyQt6.QtCore import pyqtSignal, QThread

"""
            Truc a faire / fonctionalité requise

 1- gravité universelle (gravité en fonction le l'attraction des corps)
 2- gestion des collisions
 3- play/pause/stop/restart
 4- ajout d'un object

 """
class Thread(QThread):
    pass

class Simulation_model:
    planets = []
    model_changed = pyqtSignal(list)

    def __init__(self):
        self.create_sim()

    def create_sim(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.default_planets()

        self.model_changed(self.planets)

    def default_planets(self):
        self.add_planet()
        self.add_planet(120, 0, 0, 60, 20, 10, "rouge")

    def add_planet(self, x = 0, y = 0, vx = 0, vy = 10, masse = 10, rayon = 12, couleur = "bleu"):
        body = pymunk.Body(masse, pymunk.moment_for_circle(masse, 0, rayon))
        body.position = (x, y)
        body.velocity = (vx, vy)

        shape = pymunk.Circle(body, rayon)
        shape.color = couleur

        self.space.add(body, shape)
        self.planets.append(body)

        self.model_changed(self.planets)

    def step(self, dt):
        G = 2000
        n = len(self.planets)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = self.planets[i]
                p2 = self.planets[j]
                b1 = p1.body
                b2 = p2.body

                dx = b2.position.x - b1.position.x
                dy = b2.position.y - b1.position.y
                dist_sqrt = dx * dx + dy * dy

                if dist_sqrt == 0:
                    continue

                dist = math.sqrt(dist_sqrt)
                force_grav = G * b1.mass * b2.mass/ dist_sqrt

                fx = force_grav * dx / dist
                fy = force_grav * dy / dist

                b1.apply_force_at_local_point(fx, fy)
                b2.apply_force_at_local_point(-fx, -fy)

        self.space.step(dt)

    def reset_model(self):
        self.__init__()