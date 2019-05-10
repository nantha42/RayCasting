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
            self.walls.append(Boundary(x1,y1,x2,y2))
        self.walls.append(Boundary(0,0,700,0))
        self.walls.append(Boundary(0, 0, 0, 700))
        self.walls.append(Boundary(0, 700, 700, 700))
        self.walls.append(Boundary(700, 0, 700, 700))
        self.particle = Particle()
        self.stopgame = False

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

            py.display.update()


if __name__ == '__main__':
    D = Display()
    D.run()
