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
class Planet:
    __position = None
    __masse = None
    __radius = None
    __velocity = None

    def __init__(self, x, y, masse, radius, vx, vy):
        self.position = x, y
        self.masse = masse
        self.radius = radius
        self.velocity = vx, vy

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def masse(self):
        return self.__masse

    @masse.setter
    def masse(self, value):
        self.__masse = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        self.__velocity = value


class Simulation_model(QObject):

    def __init__(self):
        super().__init__()
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        self.dt = 1/60
        self.time = 0

        self.planets = []
        self.rad = []
        self.data = {}


        self.add_planet()
        self.add_planet(100, 100, 100, 20, -10, 10)


    def add_planet(self, x=0, y=0, mass=100, radius=10, vx=0, vy=0):
        body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        body.position = x, y
        body.velocity = (vx, vy)

        shape = pymunk.Circle(body, radius)
        shape.collision_type = 1

        self.space.add(body, shape)

        self.planets.append(body)
        self.rad.append(radius)
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

    def step(self, dt):
        self.apply_gravity()
        self.space.step(dt)
        self.time += dt

        for planet in self.planets:
            self.data[planet]["position"].append(
                (self.time, planet.position.length)
            )

            self.data[planet]["velocity"].append(
                (self.time, planet.velocity.length)
            )

            a = planet.force.length / planet.mass
            self.data[planet]["acceleration"].append((self.time , a))

    def reset(self):
        self.space.remove()
        self.planets.clear()
        self.time = 0
        self.__init__()

    def get_planets(self):
        return self.planets

    def get_rad(self, i):
        return self.rad[i]