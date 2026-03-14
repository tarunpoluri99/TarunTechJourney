'''
Q3. Create an Employee class that:
•	Keeps a minimum experience required for promotion (shared across all employees).
•	Stores employee name, experience, and department.
•	Has a method to check eligibility for promotion.
•	Provides a function to update promotion criteria globally.
•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
'''

class Employee:
    minimum_experience=10
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def check_eligibility(self):
        return self.experience>=Employee.minimum_experience
    @staticmethod
    def is_valid(s):
        valid=["HR","Tech","Admin"]
        if s in valid:
            return True
        else:
            return False
e1=Employee("Tarun",15,"Tech")
print(e1.check_eligibility())
print(e1.is_valid(e1.department))


