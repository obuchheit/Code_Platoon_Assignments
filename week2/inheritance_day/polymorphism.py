'''
Ability to respond to the same method in different ways

'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow"

class Duck(Animal):
    def speak(self):
        return "quack"

# donald = Duck()
# gus = Cat()
# milo = Dog()

# my_animals = [donald, gus, milo]

# for a in my_animals:
#     print(a.speak())

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    PI = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return Circle.PI * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
my_circle = Circle(5)
print(my_circle.area())