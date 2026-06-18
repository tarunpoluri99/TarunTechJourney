'''
Armstrong Number: 2,3,4,5,6,7,8,9,153...

-> Sum of power of their decimal count is equal to n
-> Then it's an Armstrong Number
ex:
    n=153
    dc=3
    sum = 1^3+5^3+3^3
        => 1+125+27
        => 153
    sum==n => Arm strong Number

'''

def isarm(n):
    t=n
    dc=0
    su=0
    while t>0:
        dc+=1
        t=t//10
    t=n
    while t>0:
        r=t%10
        su=su+pow(r,dc)
        t=t//10
    return su==n
n=int(input())
n=abs(n)
if n==0:
    print("Invalid Input")
else:
    if isarm(n):
        print("Armstrong Number")
    else:
        print("Not a Armstrong Number")
