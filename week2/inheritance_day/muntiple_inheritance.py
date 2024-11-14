class Mother:
    def __init__(self):
        print('Moter.__init__()')
        self.first_name = 'Connie'
        self.last_name = 'Skornia'

class Father:
    def __init__(self):
        print('Father.__init__()')
        self.first_name = 'Jeff'
        self.last_name = 'Buchheit'

class Child(Father, Mother):
    def __init__(self, first_name):
        print('Child.__init__()')
        Father.__init__(self)
        
        self.first_name = first_name

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

owen = Child('Owen')
print(owen)



#COMPOSITION

class Engine:
    def __init__(self, type='gas'):
        self.type = type

    def start(self):
        return "Engine Started"

class Wheel:

    def __init__(self, wheel_position):
        self.wheel_postion = wheel_position

    def rotate(self):
        return "Wheel rotating"

class Car:
    def __init__(self):
        self.engine = Engine()

    def __repr__(self) -> str:
        return f"Engine type: {self.engine.type}"

taco = Car()
print(taco)