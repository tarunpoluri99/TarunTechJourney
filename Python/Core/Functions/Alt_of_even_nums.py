
from Python.Core.Functions.Even_Number import is_even

s=int(input())
e=int(input())
if s<e:
    c=0
    for i in range(s,e+1):
        res=is_even(i)
        if res==1:
            c=c+1
            if c%2==1:
                print(i)
else:
    print("Invalid Range")
