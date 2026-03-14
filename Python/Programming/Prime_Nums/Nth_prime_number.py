def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2

n=int(input())
c=0
i=2
while True:
    if isprime(i):
        c+=1
        if c==n:
            print(i)
            break
    i+=1
