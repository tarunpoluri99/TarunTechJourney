'''
Create a class person with instance variables Name,age,phone:bool.
if they have phone then class.level total_no_of phones should increase.
'''


class Person:
    total_no_of_phones=0
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        if phone:
            Person.total_no_of_phones+=1

p1=Person("Tarun",22,9381)
p2=Person("Kiran",21, 12)

print(Person.total_no_of_phones)
