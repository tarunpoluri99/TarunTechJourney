# Writing a program to print next prime number to the given prime number
# if n=14 the next prime number to 14 is 17
# prime number => 2,3,5,7,11,13,17 Here the nis 14  the first prime after 14 is 17..
# so next prime to 14 is 1


def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
n=int(input())  #n-> 14
i=n+1           #i->14+1=15,16,17
while True:
    if isprime(i):  #isprime(15),#isprime(16),isprime(17)
        print(i)      # 17 break
        break
    i+=1


