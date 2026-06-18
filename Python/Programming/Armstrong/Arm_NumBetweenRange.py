# 1
# 100
# Armstrong Numbers between the Given Values are 2, 3, 4, 5, 6, 7, 8, 9.

def isarm(n):
    t=n
    dc=0
    while t>0:
        dc+=1
        t=t//10
    t=n
    su=0
    while t>0:
        r=t%10
        su=su+pow(r,dc)
        t=t//10
    return su==n
s=int(input())
e=int(input())
s=abs(s)
e=abs(e)
c=0
if s==0 or e==0:
    print("Invalid Inputs")
else:
    if s>e:
        s,e=e,s
    for i in range(s+1,e):
        if isarm(i):
            c+=1
            if c==1:
                print("Armstrong Numbers between the Given Values are",end=" ")
            if c!=1:
                print(", ",end="")
            print(i,end="")
    if c==0:
        print("No Armstrong Numbers between the Given Values.")
    else:
        print(".")

