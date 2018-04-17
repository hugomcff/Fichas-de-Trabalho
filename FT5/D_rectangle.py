"""
Example
"""

from C_point import Point

class Cubo():

    def __init__(self, point1, tamanho):
        self.point1 = point1
        self.tamanho = tamanho

    def __str__(self):
        return "Rectangle corners:\n{}\n{}".format(self.point1, self.tamanho)

    def get_size(self):

        return Point(abs(self.point1.x), abs(self.point1.y), abs(self.point1.z) )


if __name__ == "__main__":
    
    p1 = Point(0, 0, 0)
    tamanho = 5

    cubo = Cubo(p1, tamanho)
    
    print(cubo)
