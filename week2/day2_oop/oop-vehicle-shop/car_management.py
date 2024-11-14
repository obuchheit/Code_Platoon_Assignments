


class CarManager:
    all_cars = {}
    total_cars = 0
    id_counter = 1

    # @classmethod
    # def prompt_user_to_add_car(cls):
    #     make = input()
    #     model = input()
    #     year = int(input())
    #     milage = int(input())
    #     service_item = input()

    #     #CarManager()
    #     cls(make, model, year, milage, service_item)

    def __init__(self, name, make='', model='', year=None, milage=None, services=[]):
        self.name = name
        self._make = make
        self._model = model
        self._year = year
        self._milage = milage
        self._services = services
        self._id = CarManager.id_counter

        CarManager.all_cars[self._id] = self
        CarManager.total_cars += 1
        CarManager.id_counter += 1
        print(self)

    def add_service(self, service):
        self._services.append(service)
        print(f'{service} was added to {self.name}')

    def update_milage(self, milage):
        self._milage = milage

    def __str__(self):
        return f'Car make: {self._make}, Car model: {self._model}, Car year: {self._year}. Car milage: {self._milage}, Car services: {self._services} '
    





        
        
        
        

