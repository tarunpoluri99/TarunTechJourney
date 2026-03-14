'''
Q10. Create a class Member that:
•	Has a shared BMI limit for “fit” status.
•	Each member stores name, height, weight.
•	Has a method to calculate BMI and check fit status.
•	Provides a function to update BMI limit for all members.
•	Offers a tool to check if height and weight entered are valid numbers.
'''

class Member:
    bmi_limit=25
    def __init__(self,n,h,w):
        self.name=n
        self.height=h
        self.weight=w


    def calculate(self):
        cal=self.height/self.weight
        if cal>=self.bmi_limit:
            print("unfit")
        else:
            print("Fit")
    @classmethod
    def update(cls,new):
        cls.bmi_limit=new

    @staticmethod
    def valid(h,w):
        return h>0 and w>0

m1=Member("Tarun",23,50)
m1.calculate()
m1.update()