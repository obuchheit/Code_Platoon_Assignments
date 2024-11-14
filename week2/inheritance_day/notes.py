'''
INHERITENCE:
-What is inheritance
-How to use inheritance
-When to use it
'''


'''
Inheritence is for a "is-a" relationship
Composition is for a "has-a" relationship
'''

class Animal:
    def __init__(self, name, species, sound):
        self.name = name 
        self.species = species
        self.sound = sound

    def __repr__(self) -> str:
        return f'{self.name} is a {self.species}'
    
    def eat(self):
        print(f'{self.name} eats.')

    def make_sound(self):
        print(f'{self.name} says {self.sound}')

        

    
class Dog(Animal):
    def __init__(self, name, breed):
        #returns the parent class
        super().__init__(name, "Dog","Woof")
        self.breed = breed

    
daryl = Dog('daryl', 'Lab')
print(daryl)
print(daryl.__dict__)
# print(dir(daryl))


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat","Meow")
        self.color = color
        self.sound = 'Meow'



gus = Cat('gus', 'black')
print(gus)
print(gus.__dict__)
gus.make_sound()
daryl.make_sound()