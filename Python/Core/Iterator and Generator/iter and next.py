# Iterator is used for generating iterating values
# Iter and next method are used for lazy programming.
# This helps to point one by one only when it's called
# iter-> iteration of value
# next-> for pointing the next value after iteration
# l=[1 2 3 4 5]
# it=iter(l) # iterates list values as 1 2 3 4 5
# print(next(it)) # 1  i.e., moves pointer from none to 1
# print(next(it))  # 2  i.e., moves pointer from 1 to 2

class A:
    def __init__(self):
        self.c=0
    def __iter__(self):
        return self

    def __next__(self):
        if self.c>=5:
            raise StopIteration
        self.c+=1
        return self.c

obj=A() # object created
it=iter(obj) #iter method called
print(next(it)) # next method called , so c=1
print(next(it)) # c=2
print(next(it)) # c=3
print(next(it)) # c=4



