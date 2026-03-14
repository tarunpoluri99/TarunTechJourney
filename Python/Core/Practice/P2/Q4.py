'''
Q4. Create a class Car with:
•	instance attribute mileage
•	class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.'''

class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage

    def display_specs(self):
        print("Mileage: ",self.mileage)
        print("Wheels: ",Car.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels

# Creating an object with mileage
c1=Car("28 kmph ")
c2=Car("30 kmph ")

#Calling IM()->display_specs using objects
c1.display_specs()
c2.display_specs()
#Calling IM()->display_specs using ClassName
Car.display_specs(c1)
Car.display_specs(c2)

# To change Car wheels => we using Class Method() -> Change_wheels
print(Car.wheels) # 4

Car.change_wheels(8)

print(Car.wheels) #8