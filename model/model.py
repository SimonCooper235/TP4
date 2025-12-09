import math
import threading
import time

import pymunk
from PyQt6.QtCore import pyqtSignal, QThread, QObject

from test import screen

"""
            Truc a faire / fonctionalité requise

 1- gravité universelle (gravité en fonction le l'attraction des corps)
 2- gestion des collisions
 3- play/pause/stop/restart
 4- ajout d'un object

 """
class Thread(threading.Thread):
    etat = pyqtSignal(bool)

    def run(self):
        self.etat.emit(True)



class Simulation_model(QObject):
    planets = []
    model_changed = pyqtSignal(list)
    running = False

    def __init__(self):
        super().__init__()
        self.create_sim()

    def create_sim(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.default_planets()
        self.simuler()

        self.model_changed.emit(self.planets)

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

        self.model_changed.emit(self.planets)

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

    def simuler(self):
        running = True
        self.simulation = Thread()
        self.simulation.etat.connect(self.etat)
        self.simulation.finished.connect(self.reset_model)
        self.simulation.start()

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