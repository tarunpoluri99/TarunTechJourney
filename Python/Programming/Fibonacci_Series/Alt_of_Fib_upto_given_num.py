# Alternative Fibonacci Series upto Given Number
# Fibonacci Series  -> 0 1 1 2 3 5 8 13 21 34 ...
# Alt of Fib_Series -> 0 1 3 8 21 .....

# if n=5 => fib series = 0 1 1 2 3
#        => Alt fib_series = 0 1 3

n=int(input())
a,b=0,1
count=0
ac=0

# Writing using while and for loop

while a<n:
    count+=1
    if count%2==1:
        print(a, end=" ")
        ac+= 1

    c=a+b
    a=b
    b=c

# for i in range(1,n+1):
#     count+=1
#     if count%2==1:
#         print(a,end=" ")
#         ac+=1
#
#     c=a+b
#     a=b
#     b=c