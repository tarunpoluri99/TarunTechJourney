'''
Create a class Building
with class_Variable no_of_rooms with some default value and instance variable
Building_name and wifi: bool. Every time object is created the total_no_of_building's
counter should increase '''

class Building:
    no_of_rooms=0
    total_no_of_buildings=0
    def __init__(self,building_name,wifi):
        self.name=building_name
        self.wifi=wifi
        Building.total_no_of_buildings+=1
b1=Building("Manikanta",123)
b2=Building("sri Srinivasa",0)

print(Building.total_no_of_buildings)
