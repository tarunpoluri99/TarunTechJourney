'''
Q9. Create a class BankAccount with:
•	class variable bank_name
•	instance variables holder and balance
•	instance method deposit(amount)
•	class method change_bank_name(cls, new_name)
•	static method validate_amount(amount) → returns True if amount > 0
Show transactions and how static + class methods work together.
'''

class BankAccount:
    bank_name="CvBank"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    #IM()
    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
        return self.balance

    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        return amount>0
b1=BankAccount("Tarun",10000)
b2=BankAccount("kiran",230000)

print("Before depositing, b1 balance is: ",b1.balance)
b1.deposit(1000)
print("After depositing, b1 balance is: ",b1.balance)
print()
print("Before changing b1 bank name is: ",b1.bank_name)
BankAccount.bank_name="Pybank"
print("After changing b1 bank name is : ",b1.bank_name)
print()
print("Is b1 balance is valid : ",b1.validate_amount(b1.balance))
