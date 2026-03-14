# writing a prgm to print First n Prime Numbers
# if n=5 => prime numbers -> 2 3 5 7 11 ....
# First 1 prime means 2, First 2nd prime is 3...
# Prime first n numbers means Count==n

def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
n=int(input())  # n=5,c=0,i=2 bcuz the first prime num is 2
c=0
i=2

while c<n:  # o<5(T) ... 1<5(T)...2<5(T)...3<5(T)...4<5(T)...5<5(False)
    if isprime(i):  # isprime(2),isprime(3)...isprime(11)
        c=c+1       # 1 2 3 4 5
        print(i,end=" ") # 2 3 5 7 11
    i+=1    # 2,3,4,5...11