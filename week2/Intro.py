

class Dog:
    # Double underscores indicate programmers should NOT call this method directly
    def __init__(self, name, breed):
        print(f'Hello {name}, you are a {breed}.')

        self.name = name
        self.breed = breed

    def speak(self):
        print(f'{self.name} says: Bark')
    
    def fetch(self, item):
        print(f'{self.name} has fetched the {item}')

    #Prints out the class object into a string rather than where it is in memory
    def __str__(self):
        return f'Name: {self.name} Breed: {self.breed}'
    


# Construction an instance of a class: aka Instantiating a class instance. Calls the init method
'''fido = Dog('Fido', 'Belgian')
rover = Dog('Rover', 'Bloodhound')


rover.speak()
rover.fetch('Ball')
fido.fetch('stick')

#Instantiates __str__ method
print(rover)
'''

class Cat:
    def __init__(self, name, color='black', sound='Meow'):
        self.name = name
        self.color = color
        self.sound = sound

    def __str__(self) -> str:
        return f'Name: {self.name}, Color: {self.color}'
    


def my_decorator(func):
    print('inside my_decorator()')

    def wrapper_function():
        print('Todays greeter wants to say a message ...')
        func() # call the function passed in as an arg
        print('... the message has been delivered.')

    return wrapper_function

@my_decorator
def say_hi():
    print('hello, world.')

say_hi()
    

#getters and setters are good for: -validating data, formatting data, and applying other logic to data


class Person:
    #class attributes: adds attribute to the class 

    legs = 2
    eyes = 2
    has_a_concious = True
    id_counter = 1
    all_persons = []


    def __init__(self, name, age):
        self._name = name 
        self._age = age
        #shows how many instances were made in the id_counter
        Person.id_counter += 1
        Person.all_persons.append(self)

    # Getter
    @property
    def name(self):
        return self._name.capitalize()
    
    # Setter
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str and len(new_name) >= 3):
            self._name = new_name
        else:
            print('Name must be a string at least 3 chars long.')

    def __repr__(self):
        pass


alice = Person('alice', 20) 
print(alice.name) 

alice.name = 'bob'

print(alice._name) #bob
print(alice.name) #Bob



    


