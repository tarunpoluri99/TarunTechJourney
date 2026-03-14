''' Q5. Create a class Temperature with:
•	instance attribute celsius
•	a static method to_fahrenheit(celsius)
•	an instance method show_conversion() that uses the static method to print both values.
'''

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(c):
        return (c*9/5)+32
    #Instace Method()
    def show_conversion(self):
        print("Celsius: ",self.celsius)
        print("Fahrenheit: ",Temperature.to_fahrenheit(self.celsius))
t1=Temperature(37)
t2=Temperature(39)
# Calling Static method() using object t1 and t2
t1.show_conversion()
t2.show_conversion()
print()
# Calling Static Method using ClassName by specifying the object in it
Temperature.show_conversion(t1)
Temperature.show_conversion(t2)
