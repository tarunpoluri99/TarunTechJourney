# First n alternative fibonacci numbers
# Alternative Fibonacci Series = 0 1 3  8  21 55 144....
# first 1 terms is 0, 2 terms is 0 1 ,3 terms is 0 1 3, n terms is 0 1 3 ... n
# if n=5 => 0 1 3 8 21

n=int(input())
a,b=0,1
count=0
ac=0
# Writing using while loop and for loop

while ac<n:
    count+=1
    if count%2==1:
        print(a,end=" ")
        ac+=1
    c=a+b
    a=b
    b=c

# for i in range(1,2*n+1):
#     count+=1
#     if count%2==1:
#         print(a,end=" ")
#     c=a+b
#     a=b
#     b=c