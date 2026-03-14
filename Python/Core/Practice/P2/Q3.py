'''
Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance. '''
class MathOps:  # Class

    @staticmethod
    def is_even(num): # Static Method() doesn't need cls or self
        return num%2==0

b1=MathOps() # object created but not initialized
b2=MathOps() #same

print(MathOps.is_even(34)) # Giving parameter directly to the Static Method() with class
print(b1.is_even(28)) # Giving parameter directly to SM() after object creation using obj