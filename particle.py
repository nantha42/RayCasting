from numpy import array
from numpy import deg2rad
from numpy import linalg
from pygame.draw import line
from pygame.draw import circle
from ray import *


class Particle:
    def __init__(self):
        self.pos = array([250, 250])

    def show(self, win):
        circle(win, (255, 255, 255), self.pos, 1, 1)
        for ray in self.rays:
            ray.show(win)

    def look(self, win, walls):
        self.rays = []
        for i in range(0, 360, 5):
            self.rays.append(Ray(self.pos[0], self.pos[1], deg2rad(i)))

        for ray in self.rays:
            closest = 10000000
            closestpt = None
            for wall in walls:
                pt = ray.cast(wall)

                if pt is not None:
                    dis = linalg.norm(pt - self.pos)
                    if (dis < closest):
                        closest = dis
                        closestpt = pt

            if closestpt is not None:
                line(win, (255, 255, 0), self.pos, array(closestpt, int), 2)
