'''
Q4. Build a Loan class that:
•	Has a common interest rate for all loans.
•	Each object stores borrower name and principal.
•	Calculates total payable amount.
•	Provides a function to update the interest rate.
•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
'''
from code import interact


class Loan:
    interest_rate=10
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def total_amount(self):
        return self.principal*Loan.interest_rate
    @classmethod
    def update_ir(cls,new_rate):
        cls.interest_rate=new_rate
        return cls.interest_rate

l1=Loan("Tarun",1000)
print(f"{l1.name}'s loan ammount at {Loan.interest_rate} is: ",l1.total_amount())
Loan.update_ir(20)
print(f"{l1.name}'s loan ammount at {Loan.interest_rate} is: ",l1.total_amount())


