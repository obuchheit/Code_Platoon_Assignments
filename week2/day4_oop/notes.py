"""
Intro to Data Structures and Algorithms

-Simple Search
-Binary Search
"""
import csv
#Binary Search

def binary_search(lst, target):
    steps = 0 

    low = 0
    high = len(lst) - 1

    while low <= high:
        steps += 1
        mid = (low + high) // 2 #Round down if mid is x.5
        print(f'STEP: {steps} | low: {low} | mid: {mid} | high: {high}')

        if lst[mid] == target:
            return mid, steps
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    #If not found
    return -1, steps

# my_list = list(range(1000000))

# target_index, num_steps = binary_search(my_list, 8809)

# print(my_list[target_index])

'''
School OOP review
data
classes dir
runner.py



When working with a csv file and a class; Take the header of the csv file and use those as the class elements.

** Argument:
dict = {}

obj = ClassName(**dict)


-When using a runner you have to fix the path issues when opening a file.
-Each feature you add make sure you test every other feature that has been built to make sure no bugs were introduced.
'''

class Student:
    def __init__(self, name, age, role, school_id, password):
        self.name = name
        self.age = age
        self.role = role
        self.school_id = school_id
        self.password = password


    def __repr__(self) -> str:
        return f'Name: {self.name} Age: '
        '''Adds all rows of data as the '''
    @classmethod
    def all_students(cls):
        students = []
        with open('../data/students') as student_file:
            reader = csv.DictReader(student_file)
            students = [cls(**x) for x in reader] #Would need to add index for tpms 
            return students
        
print(Student.all_students())
        #     for row in reader:
        #         students.append(cls(**row))
        # print(students)



    # @classmethod
    # def create_student(cls):
    #     def capture_age():
            
        #     age = input("Enter age here: ")
        #     if type(age) == int:
        #         return age 
            
    #     new_student = {
    #         "name": 
    #         "age":
    #     }
    
    
    #Test 4 Error
