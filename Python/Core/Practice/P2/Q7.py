'''
Q7. Create a class Employee with:
•	instance attributes: name, base_salary
•	class variable: bonus_rate = 0.1
•	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
•	class method: update_bonus(cls, new_rate) → updates bonus for all employees
•	static method: is_valid_salary(sal) → checks if salary > 0
Create two employees, show final salaries, update bonus rate, and show again.
'''

class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    #Instance Method()
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)

    @classmethod
    def update_bonus(cls,new_rate):
        cls.new_rate=new_rate
        Employee.bonus_rate+=new_rate
        return Employee.bonus_rate

    @staticmethod
    def is_valid_salary(sal):
        return sal>0

e1=Employee("Tarun",50000)
e2=Employee("Kiran",75000)

print(e1.final_salary())
print(e1.update_bonus(2.9))
print((e1.final_salary()))
print(e1.is_valid_salary(e1.base_salary))
print()
print(f"e2 final salary with {Employee.bonus_rate} :",e2.final_salary())
print("Bonus rate increment: ",e2.update_bonus(3.0))
print(f"e2 final salary with {e2.bonus_rate} :",e2.final_salary())
print(f"e2 salary of {e2.base_salary} is valid : ",e2.is_valid_salary(e2.base_salary))


