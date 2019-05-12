import pygame as py
import numpy as np
from boundary import *
from particle import *



class Display:
    def __init__(self):
        py.init()
        np.random.seed(1)
        self.win = py.display.set_mode((700, 700))
        self.walls = []
        self.up,self.down,self.right,self.left = 0,0,0,0

        for i in range(5):
            x1 = np.random.randint(0,700)
            y1  = np.random.randint(0, 700)
            x2 = np.random.randint(0, 700)
            y2 = np.random.randint(0, 700)
            x3 = np.random.randint(0, 700)
            y3 = np.random.randint(0, 700)
            #self.walls.append(Boundary(x1,y1,x2,y2))
            #self.walls.extend(self.box(x3,y3))

        #N
        self.walls.append(Boundary(10,400, 50, 250))
        self.walls.append(Boundary(50, 250, 90, 400))
        self.walls.append(Boundary(90, 400, 130, 250))
        #A
        self.walls.append(Boundary(150,400,190,250))
        self.walls.append(Boundary(190,250,230,400))
        self.walls.append(Boundary(170, 330, 210, 330))
        #N
        self.walls.append(Boundary(10+240, 400, 50+240, 250))
        self.walls.append(Boundary(50+240, 250, 90+240, 400))
        self.walls.append(Boundary(90+240, 400, 130+240, 250))
        #T
        self.walls.append(Boundary(390, 250, 470,250))
        self.walls.append(Boundary(430, 250, 430, 400))
        #H
        self.walls.append(Boundary(490,250,490,400))
        self.walls.append(Boundary(570, 250, 570, 400))
        self.walls.append(Boundary(490,325,570,325))
        #A
        d = 440
        self.walls.append(Boundary(150+d, 400, 190+d, 250))
        self.walls.append(Boundary(190+d, 250, 230+d, 400))
        self.walls.append(Boundary(170+d, 330, 210+d, 330))
        #K
        self.walls.append(Boundary(690, 400, 690, 250))
        self.walls.append(Boundary(690, 325, 770, 250))
        self.walls.append(Boundary(690, 325, 770, 400))

        self.walls.append(Boundary(0,0,700+70,0))
        self.walls.append(Boundary(0, 0, 0, 700+70))
        self.walls.append(Boundary(0, 700+70, 700+70, 700+70))
        self.walls.append(Boundary(700+70, 0, 700+70, 700+70))
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
        #for wall in self.walls:
        #  wall.show(self.win)
        self.particle.show(self.win)
    def update(self):
        if self.up:
            self.particle.pos[1]-=3
        if self.down:
            self.particle.pos[1]+=3
        if self.left:
            self.particle.pos[0]-=3
        if self.right:
            self.particle.pos[0]+=3
    def run(self):
        while not self.stopgame:
            self.win.fill((0, 0, 0))
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.stopgame = True
                if event.type == py.MOUSEMOTION:
                    pos = np.array(event.pos)
                    d = (pos-self.particle.pos)
                    d = d/np.linalg.norm(d)

                    theta = np.arccos(d[0])
                    deg = np.rad2deg(theta)

                    angle = deg
                    if d[0]>=0:
                        if d[1] >=0:
                            #1 quadrant
                            angle = deg

                        elif d[1]<0:
                            #4 qudarant
                            angle = -deg

                            pass

                    else:
                        if d[1] >=0:
                            #2 quadrant
                            angle = deg
                        else:
                            angle = -deg
                    print(angle)

                    self.particle.lookangle = angle

                if event.type == 2:
                    if event.key == py.K_w:
                        self.up = 1
                    if event.key == py.K_a:
                        self.left = 1
                    if event.key == py.K_d:
                        self.right = 1
                    if event.key == py.K_s:
                        self.down = 1
                if event.type == 3:
                    if event.key == py.K_w:
                        self.up = 0
                    if event.key == py.K_a:
                        self.left = 0
                    if event.key == py.K_d:
                        self.right = 0
                    if event.key == py.K_s:
                        self.down = 0
            self.update()
            self.particle.look(self.win,self.walls)
            self.draw()
            self.clock.tick(100)
            py.display.update()

if __name__ == '__main__':
    D = Display()
    D.run()
