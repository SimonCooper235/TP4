from msilib.schema import Property

import pymunk

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
        self.body = pymunk.Body(masse, pymunk.moment_for_circle(masse, 0, radius))
        self.body.position = (x, y)
        self.body.velocity = (vx, vy)

        self.position = (x, y)
        self.masse = masse
        self.radius = radius
        self.velocity = (vx, vy)

        self.shape = pymunk.Circle(self.body, radius)

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


class Simulation_model():
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.planets = []
        self.add_planet()
        self.time = 0

    def add_planet(self, x=0, y=0, mass=10, radius=10, vx=0, vy=0):
        self.planets.append(Planet(x, y, mass, radius, vx, vy))

    def apply_gravity(self):
        for i, p1 in enumerate(self.planets):
            for p2 in self.planets[i+1:]:
                delta = p2.body.position - p1.body.position
                dist = delta.length + 1e-5
                force = 400 * p1.body.mass * p2.body.mass / dist**2
                direction = delta.normalized()
                p1.body.apply_force_at_world_point(force * direction, p1.body.position)
                p2.body.apply_force_at_world_point(-force * direction, p2.body.position)

    def step(self, dt):
        self.time += dt
        self.apply_gravity()
        self.space.step(dt)

    def reset(self):
        self.space.remove()
        self.planets.clear()
        self.time = 0

    def get_planets(self):
        return self.planets