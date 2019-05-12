from numpy import array
from pygame.draw import line


class Boundary:
    def __init__(self, x1, y1, x2, y2):
        div = 1.1
        self.a = array((x1/div, y1/div))
        self.b = array([x2/div, y2/div])

    def show(self, surf):
        line(surf, (255, 255, 255), self.a, self.b, 2)
