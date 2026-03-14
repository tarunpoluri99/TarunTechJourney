'''
# Lcm of 3 Numbers => lcm(2,3,10) is 30
-> 2 multiples-> 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
-> 3 multiples -> 3, 6, 9, 12,15,18,21,24,27,30,33,
-> 10 multiples-> 5,10,15,20,25,30,35,40,45,50
-> Common Factor : 30...
-> Least common multiple  is 30
'''
import math
a=int(input())
b=int(input())
c=int(input())
m=max(a,b,c)
n=m
while True:
    if m%a==0 and m%b==0:
        if m%c==0:
            print(m)
            break
    m=m+n