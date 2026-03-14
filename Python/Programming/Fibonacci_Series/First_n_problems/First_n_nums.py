# first n fibonacci numbers
# Fibonacci Series = 0 1 1 2 3 5 8 13 21 34 55 89 144
# if n=5 => 0 1 1 2 3

n=int(input())
a,b=0,1
c=0
for i in range(1,n+1):
    c+=1
    print(a,end=" ")
    c=a+b
    a=b
    b=c