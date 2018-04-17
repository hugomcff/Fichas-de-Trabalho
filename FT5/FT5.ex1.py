
class Rectangle():

    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    def get_size(self):
        return Point(abs(self.point2.x - self.point1.x), abs(self.point2.y - self.point1.y) )

    def __str__(self):
        return "Pontos do cubo:\n{}\n{}".format(self.point1, self.point2)

if __name__ == "__main__":
    
    p1 = Point(2, 3, "red")
    p2 = Point(10, 20)

    rectangle = Rectangle(p2, p1)
    
    print(rectangle)

    print(rectangle.get_size())