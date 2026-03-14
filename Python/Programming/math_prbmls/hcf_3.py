'''
Lcm of 3 Numbers:
-> lcm(10,6,8)
Here,
-> min value is 6
-> common factors for 10,6,8 is -> 1 2
-> highest common factor is 2
'''

import math
a=int(input())
b=int(input())
c=int(input())
m=min(a,b,c)
i=0
while True:
    n=m-i
    if a%n==0 and b%n==0:
        if c%n==0:
            print(n)
            break
    i=i+1
