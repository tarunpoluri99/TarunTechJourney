def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc=fc+1
    if fc==2:
        return True
    else:
        return False
s=int(input())
e=int(input())

if s>0 and e>0:
    pc=ac=0
    for i in range(s,e+1):
        b=is_prime(i)
        if b==True:
            pc=pc+1
            if pc%2==1:
                ac=ac+1
                print(i,end=" ")
else:
    print("Invalid Inputs")
