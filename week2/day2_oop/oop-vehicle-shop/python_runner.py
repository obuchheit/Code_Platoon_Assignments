from car_management import CarManager



def main():
    while True:
        name = ''
        cars_dict = {}


        add_or_service = input("Are we servicing an existing customers car or adding a customer?\n Enter <new> or <return>: ")

        if add_or_service == 'new':
            name = input('What is their full name?\nEnter here: ')
            name = name.lower()
            name = name.replace(" ", "")

            make = input('Enter car make: ')
            model = input('Enter car model: ')
            year = int(input('Enter car year: '))
            milage = int(input('Enter the cars milage: '))
            service = [input('Add todays service: ')]

            cars_dict[name] = CarManager(name, make, model, year, milage, service)

        else:
            name = input('What is their full name?\nEnter here: ')
            name = name.lower()
            name = name.replace(" ", "")

            milage = input('How many miles are on the car now? ')
            service = input('Add todays service: ')

            cars_dict[name].add_service(service)
            cars_dict[name].update_milage(milage)


        for key in cars_dict.values():
            print(key)




andielizabeth = CarManager('andielizabeth', 'Ford', 'Escape', 2015, 120000, ['oil change', 'tires'])


main()
