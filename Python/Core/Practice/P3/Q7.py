'''
Q7. Build an Inventory class that:
•	Tracks the total number of items across all inventories.
•	Each instance maintains its own stock dictionary ({"item": quantity}).
•	Provides a method to add or remove stock.
•	Allows updating a minimum stock threshold globally.
•	Offers a static checker to verify if a stock level is below threshold.
'''
class Inventory:
    total_items=0
     threshold=3
     def __init__(self):
         self.stock=dict({})

     def add(self,k,v):
         self.stock[k]=v
         Inventory.total_items+=1
     def remove(self,k):
         self.stick.pop(k,None)
         Inventory.total_items-=1

     @classmethod
    def change(cls,new):


