# 1
# 200
# Alternative Armstrong between Given Values are: 2, 4, 6, 8, 153.
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
ac=0

if s==0 or e==0:
    print("Invalid Inputs")
else:
    if s>e:
        s,e=e,s
    for i in range(s+1,e):
        if isarm(i):
            c+=1
            if c%2==1:
                ac+=1
                if ac==1:
                    print("Alternative Armstrong between Given Values are:",end=" ")
                if c!=1:
                    print(", ",end="")
                print(i,end="")
    if c==0:
        print("No Alternative Armstrong Numbers Between Given Values.")
    else:
        print(".")