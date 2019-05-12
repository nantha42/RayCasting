from numpy import array
from numpy import deg2rad
from numpy import linalg
from pygame.draw import line
from numpy import random
from pygame.draw import circle
from ray import *


class Particle:
    def __init__(self):
        self.pos = array([250, 250])
        self.lookangle = 0

    def show(self, win):
        circle(win, (255, 255, 255), self.pos, 1, 1)
        for ray in self.rays:
            ray.show(win)

    def look(self, win, walls):
        self.rays = []

        for i in range(0, 30):
            self.rays.append(Ray(self.pos[0], self.pos[1], deg2rad(self.lookangle+i*.9)))
            self.rays.append(Ray(self.pos[0],self.pos[1],deg2rad(self.lookangle-i*.9)))

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
                line(win, (30, 30, 30), self.pos, array(closestpt, int), 1)
                x = random.randint(250, 255)
                y = random.randint(250,255)
                z = random.randint(250,255)
                circle(win,(x,y,z),array(closestpt, int),1,1)
