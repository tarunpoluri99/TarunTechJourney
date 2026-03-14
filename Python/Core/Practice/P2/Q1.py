
''' Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed. '''

class Student:
    total_students=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1
    def is_passed(self):
        return self.marks>40
s1=Student("Tarun",44)
s2=Student("Kiran",39)

# Calling is_passed IM() using object s1 and s2
print(s1.is_passed())
print(s2.is_passed())
print()

# Calling IM() using className by specifying the object
print(Student.is_passed(s1))
print(Student.total_students)

