class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name 
        self._age = age 
        self._grade = grade
        self.valid_grades = ['9th', '10th', '11th', '12th']
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name): 
        if isinstance(new_name, str):
            self._name = new_name
        else: pass

    @property
    def age(self):
        return self._age

    @age.setter 
    def age(self, new_age): 
        if isinstance(new_age, int): 
            self._age = new_age 
        else: pass

    @property
    def grade(self):
        return self._grade

    @grade.setter 
    def grade(self, new_grade):
        if isinstance(new_grade, str) and new_grade in self.valid_grades:
            self._grade = new_grade
        else: pass