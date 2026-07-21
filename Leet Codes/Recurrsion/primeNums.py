def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2

def primeNum(s,e):
    if s>e:
        return
    if prime(s):
        print(s,end=" ")
    primeNum(s+1,e)
s=int(input())
e=int(input())
primeNum(s,e)