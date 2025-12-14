import pymunk

"""
            Truc a faire / fonctionalité requise

 1- gravité universelle (gravité en fonction le l'attraction des corps)
 2- gestion des collisions
 3- play/pause/stop/restart
 4- ajout d'un object

 """
class Planet:
    def __init__(self, x, y, mass, radius, vx, vy):
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        self.body.position = (x, y)
        self.body.velocity = (vx, vy)

        self.shape = pymunk.Circle(self.body, radius)


class Simulation_model():
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.planets = []
        self.time = 0

    def add_planet(self, x=0, y=0, mass=10, radius=6, vx=0, vy=0):
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
        self.space.remove(*self.planets)
        self.planets.clear()
        self.time = 0