from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self): pass

class Rectangle(Shape):
    def draw(self):
        print("Rectangle")

class Square(Shape):
    def draw(self):
        print("Square")

class Circle(Shape):
    def draw(self):
        print("Circle")

def shape_factory(sh_type):
    if sh_type == 'circle':
        return Circle()
    if sh_type == 'rectangle':
        return Rectangle()
    if sh_type == 'square':
        return Square()
    
s = shape_factory("square")
s.draw()
    



