'''
Q10. Create a class Student with:
•	class variable passing_marks = 40
•	instance attributes name, marks
•	instance method result() → prints pass/fail using class variable
•	class method update_passing_marks(cls, new_marks)
'''

class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        if self.marks<Student.passing_marks:
            print("Fail")
        else:
            print("Pass")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
        return new_marks
s1=Student("Tarun",22)
print(f"s1 grade before updating pass marks {Student.passing_marks}: ")
s1.result()
Student.update_passing_marks(20)
print()
print(f"S1 grade after updating pass marks to {Student.passing_marks}")
s1.result()

