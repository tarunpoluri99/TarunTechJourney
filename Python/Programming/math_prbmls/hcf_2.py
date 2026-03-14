'''
hcf -> Highest common factor
hcf(6,8)-> 2
6 factors -> 1 2 3 6
6 factors -> 1, 2, 4 8
Here,
-> The lesser the num then lesser the iteration so take min(a,b) value
-> Common factor = 1 2
=> The highest common factor in both numbers is 2
'''



import math
a=int(input())
b=int(input())
m=min(a,b)
i=0
while True:
    n=m-i
    if a%n==0 and b%n==0:
        print(n)
        break
    i=i+1