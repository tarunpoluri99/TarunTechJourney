s=int(input())
e=int(input())
if s>0 and e>0:
    if s%2==0:
        c=0
        for i in range(s+1,e+1):
            if i%2==0:
                c=c+1
                if c%2==1:
                    print(i,end=" ")
    else:
        c=0
        for i in range(s,e+1):
            if i%2==0:
                c=c+1
                if c%2==1:
                    print(i,end=" ")
else:
    print("Invalid Inputs")