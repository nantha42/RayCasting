from numpy import array
from pygame.draw import line


class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = array((x1, y1))
        self.b = array([x2, y2])

    def show(self, surf):
        line(surf, (255, 255, 255), self.a, self.b, 2)
