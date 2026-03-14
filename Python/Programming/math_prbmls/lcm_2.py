'''
Lcm of 2 Numbers => lcm(2,3) is
-> 2 multiples -> 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
-> 3 multiples -> 3,6,9,12,15,18,21,24,27,30,33,
common multiples 6 12 18 24 ....
Least Common Factor is 6
'''


import math
a=int(input())
b=int(input())
m=max(a,b)
n=m
while True:
    if m%a==0 and m%b==0:
        print(m)
        break
    m=m+n