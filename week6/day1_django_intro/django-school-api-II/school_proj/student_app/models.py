from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False, unique = True)
    personal_email = models.EmailField(null = False, unique= True)
    locker_number = models.IntegerField(default=110, null = False, blank = False, unique= True)
    locker_combination = models.CharField(max_length=255, null = False, blank = False, default="12-12-12")
    good_student = models.BooleanField(default=True, blank=False)

    def __str__(self) -> str:
        return f"{self.name}-{self.student_email}-{self.locker_number}"
    
    def locker_reassignment(self, int):
        self.locker_number = int
        self.save()

    def student_status(self):
        if self.good_student:
            self.good_student = False
        else:
            self.good_student = True

        self.save()