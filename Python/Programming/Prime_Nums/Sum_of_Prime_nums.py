def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
s=int(input())
e=int(input())

if s>0 and e>0:
    sum=0
    for i in range(s,e+1):
        b=is_prime(i)
        if b==True:
            print(i,end=" ")
            sum=sum+i
    print(sum)
else:
    print("Invalid Inputs")