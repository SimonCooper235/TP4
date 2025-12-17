import math
from msilib.schema import Property

import pymunk
from PyQt6.QtCore import pyqtSignal, QObject

"""
            Truc a faire / fonctionalité requise

 1- gravité universelle (gravité en fonction le l'attraction des corps)
 2- gestion des collisions
 3- play/pause/stop/restart
 4- ajout d'un object

 """

class Simulation_model(QObject):
    data_updated = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        self.dt = 1/60
        self.time = 0

        self.planets = []
        self.rad = []
        self.couleurs = []
        self.data = {}


        self.add_planet()
        self.add_planet(100, 100, 100, 20, -10, 10)


    def add_planet(self, x=0, y=0, mass=100, radius=10, vx=0, vy=0, couleur="cyan"):
        body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        body.position = x, y
        body.velocity = (vx, vy)

        shape = pymunk.Circle(body, radius)
        shape.collision_type = 1

        self.space.add(body, shape)

        self.planets.append(body)
        self.rad.append(radius)
        self.couleurs.append(couleur)
        self.data[body] = {
            "position": [],
            "velocity": [],
            "acceleration": [],
        }


    def apply_gravity(self):
        n = len(self.planets)

        for i in range(n):
            for j in range(i+1, n):
                p1 = self.planets[i]
                p2 = self.planets[j]

                dx = p2.position.x - p1.position.x
                dy = p2.position.y - p1.position.y
                r2 = dx*dx + dy*dy + 1e-6
                r = math.sqrt(r2)

                force = 500 * p1.mass * p2.mass / r2
                fx = force * dx / r
                fy = force * dy / r

                p1.apply_force_at_world_point((fx, fy), p1.position)
                p2.apply_force_at_world_point((-fx, -fy), p2.position)

    def step(self, dt, data):
        self.apply_gravity()
        self.space.step(dt)
        if data:
            self.track_data(0)
        self.time += dt

    def track_data(self, body):
        planet = self.planets[body]

        self.data[planet]["position"].append(planet.position)

        self.data[planet]["velocity"].append(planet.velocity)

        a = planet.force.length / planet.mass
        self.data[planet]["acceleration"].append(a)

        self.data_updated.emit(self.data)

    def reset(self):
        self.space.remove()
        self.planets.clear()
        self.time = 0
        self.__init__()

    def get_planets(self):
        return self.planets

    def get_rad(self, i):
        return self.rad[i]

    def get_couleurs(self, i):
        couleur = self.couleurs[i]
        couleur_lower = couleur.lower()
        return couleur_lower