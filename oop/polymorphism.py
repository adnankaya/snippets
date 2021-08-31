"""
polymorphism gives a way to use a class exactly like its parent so
there’s no confusion with mixing types.
"""


class Figure:
    def log(self):
        print(self)

    def __str__(self) -> str:
        return self.__class__.__name__


class Circle(Figure):

    def __str__(self) -> str:
        return self.__class__.__name__


class Rectangle(Figure):
    def __str__(self) -> str:
        return self.__class__.__name__


figures = [
    Figure(),
    Circle(),
    Rectangle()
]

for figure in figures:
    figure.log()

"""
Figure
Circle
Rectangle
"""