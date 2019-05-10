import pygame as py
import numpy as np
from boundary import *
from particle import *



class Display:
    def __init__(self):
        py.init()
        self.win = py.display.set_mode((700, 700))
        self.walls = []
        for i in range(5):
            x1 = np.random.randint(0,700)
            y1  = np.random.randint(0, 700)
            x2 = np.random.randint(0, 700)
            y2 = np.random.randint(0, 700)
            x3 = np.random.randint(0, 700)
            y3 = np.random.randint(0, 700)
            self.walls.append(Boundary(x1,y1,x2,y2))
            self.walls.extend(self.box(x3,y3))
        self.walls.append(Boundary(0,0,700,0))
        self.walls.append(Boundary(0, 0, 0, 700))
        self.walls.append(Boundary(0, 700, 700, 700))
        self.walls.append(Boundary(700, 0, 700, 700))
        self.particle = Particle()
        self.stopgame = False
        self.clock = py.time.Clock()

    def box(self, x, y):
        w1 = Boundary(x, y, x + 100, y)
        w2 = Boundary(x, y, x, y + 100)
        w3 = Boundary(x + 100, y, x + 100, y + 100)
        w4 = Boundary(x, y + 100, x + 100, y + 100)
        return [w1,w2,w3,w4]

    def draw(self):
        for wall in self.walls:
            wall.show(self.win)
        self.particle.show(self.win)


    def run(self):
        while not self.stopgame:
            self.win.fill((0, 0, 0))
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.stopgame = True
                if event.type == py.MOUSEMOTION:
                    pos = event.pos
                    self.particle.pos[0] = pos[0]
                    self.particle.pos[1] = pos[1]

            self.particle.look(self.win,self.walls)
            self.draw()
            self.clock.tick(100)
            py.display.update()


if __name__ == '__main__':
    D = Display()
    D.run()
