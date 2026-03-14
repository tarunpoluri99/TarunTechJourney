'''
Q2. Design a class Product that:
•	Maintains a base tax rate applicable to all products.
•	Each product has a name and base price.
•	Has a method to compute final price including tax.
•	Can change tax rate for all products using one method.
•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
'''

class Product:
    base_tax_rate=0.1
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def final_price(self):
        self.price=self.price+Product.base_tax_rate
        return self.price

    @classmethod
    def change_tax_rate(cls,new_tax_rate):
        cls.base_tax_rate=new_tax_rate
        return cls.base_tax_rate
    @staticmethod
    def validate_price(num):
        if num>0:
            return True
        else:
            return False

p1=Product("Bottle",100)
p2=Product("Bag",500)

print(f"{p1.name} final price at {Product.base_tax_rate} is: ",p1.final_price())
print(f"{p2.name} final price at {Product.base_tax_rate} is: ",p2.final_price())
Product.change_tax_rate(1.5)
print()
print(f"{p1.name} final price at {Product.base_tax_rate} is: ",p1.final_price())
print(f"{p2.name} final price at {Product.base_tax_rate} is: ",p2.final_price())

print(p1.validate_price(p1.price))
print(p2.validate_price(p2.price))