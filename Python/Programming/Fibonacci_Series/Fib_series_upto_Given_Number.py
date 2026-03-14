# program to print fibonacci series upto given number
# if n =5 the fib values must be less n value => 0 1 1 2 3
# after 3 there is 5 but is equal to n so only upto n => 0 1 1 2 3

n=int(input())
a,b=0,1
count=0
# Writing using both for loop and while loop

for i in range(1,n+1):
    count+=1
    print(a,end=" ")

    c=a+b
    a=b
    b=c

while count<n:
    print(a,end=" ")
    count +=1

    c=a+b
    a=b
    b=c