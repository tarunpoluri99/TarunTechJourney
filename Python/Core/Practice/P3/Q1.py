'''
Q1. Create a class Student that:
•	Keeps track of the total number of students created.
•	Determines whether a student passed or failed based on a shared passing mark.
•	Provides a method to curve marks by increasing everyone’s marks by a percentage.
•	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
'''

class Student:
    total_no_of students=0
    passsing_marks=35
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    
