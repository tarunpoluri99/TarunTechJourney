a=int(input())
b=int(input())

if a==0 or b==0:
    print("Invalid Inputs")
else:
    a=abs(a)
    b=abs(b)
    if a>b:
        a,b=b,a

    ac=0
    c=0
    for i in range(a+1,b):
        t=i
        dc=0
        while t>0:
            dc+=1
            t=t//10

        t=i
        arm=0
        while t>0:
            r=t%10
            arm=arm+pow(r,dc)
            t=t//10
        if arm==i:
            ac=ac+1
            if ac%2==1:
                c=c+1
                if c==1:
                    print("Alternative Armstrong Numbers between the Given Values is", end=" ")
                if c>1:
                    print(end=", ")
                print(i,end="")
    if c==0:
        print("No Armstrong Numbers Between Given Values.")
    else:
        print(".")