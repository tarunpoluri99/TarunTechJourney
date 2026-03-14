'''
Q8. Create a class Course with:
•	class variable total_students
•	instance variable student_name
•	instance method enroll() → increments total_students
•	class method show_total(cls) → prints total students
•	static method is_eligible(age) → returns True if age ≥ 18
Demonstrate enrolling multiple students and show total count.
'''

class Course:
    total_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #IM()-> enroll()
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print("Total students: ",cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18

s1=Course("Python",21)
s2=Course("C++",19)
s1.enroll()
s2.enroll()
print(s1.is_eligible(s1.age))
print(s2.is_eligible(s2.age))
Course.show_total()