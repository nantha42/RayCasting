from numpy import array
from numpy import linalg
from pygame.draw import line
from numpy import cos,sin

class Ray:
    def __init__(self, x, y,rad):
        self.pos = array([x, y])
        self.dir = array([cos(rad), sin(rad)])

    def show(self, surf):
        line(surf, (255, 255, 255), self.pos, self.pos + self.dir * 10, 2)

    def lookAt(self, x, y):
        self.dir[0] = x - self.pos[0]
        self.dir[1] = y - self.pos[1]
        self.dir = self.dir / linalg.norm(self.dir)

    def cast(self, wall):
        x1 = wall.a[0]
        y1 = wall.a[1]

        x2 = wall.b[0]
        y2 = wall.b[1]

        x3 = self.pos[0]
        y3 = self.pos[1]

        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None
        num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        t = num / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if t > 0 and t < 1 and u > 0:
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            pot = array([x,y])
            return pot
