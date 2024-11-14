import csv


class Animals: 
   def __init__(self, animal_type): 
    try:
        with open(f'./data/{animal_type}.csv', 'r') as csv_file:
            animal_reader = csv.DictReader(csv_file, skipinitialspace=True)
            for row in animal_reader:
              age = row['age'] if row['age'] else "Unknown"  
              print(f'{row['name']} is a {age} year old{row['breed']}')
            
            
    
    except FileNotFoundError:
        print(f"Sorry we don't have any {animal_type} at our shelter.")
                
animals = Animals(input('What kind of animal are you looking for?: '))

