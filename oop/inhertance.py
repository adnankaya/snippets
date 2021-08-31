from math import pi


class Figure(object):
    def perimeter(self):
        raise NotImplementedError

    def surface(self):
        raise NotImplementedError
    
    def log(self):
        print(self)


class Circle(Figure):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def perimeter(self) -> float:
        return 2*self.radius*pi

    def surface(self) -> float:
        return pi*(self.radius**2)


class Rectangle(Figure):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def perimeter(self) -> float:
        return 2*(self.width+self.height)

    def surface(self) -> float:
        return self.width*self.height


figures = [
    Circle(2.0),
    Circle(3.0),
    Rectangle(1.0, 2.0),
    Rectangle(2.0, 5.0),
    Rectangle(3.0, 10.0)
]

for figure in figures:
    print(figure.__class__.__name__, ' : ', figure.surface())


"""Output
Circle  :  12.566370614359172
Circle  :  28.274333882308138
Rectangle  :  2.0
Rectangle  :  10.0
Rectangle  :  30.0
"""
