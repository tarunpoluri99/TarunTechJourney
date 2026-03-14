# Writing a program to print before prime number to the given prime number
# if n=10 the next prime number to 10 is 7
# prime number => 2,3,5,7,11,13,17 Here the n is 10  the first prime before 10 is 7.
# so before prime to 10 is 7


def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
n=int(input())  #n-> 10
i=n-1           #i->10-1=>9,8,7
while True:
    if isprime(i):  #isprime(9),#isprime(8),isprime(7)
        print(i)      # 7 break
        break
    i-=1


