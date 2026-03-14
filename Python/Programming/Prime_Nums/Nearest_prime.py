Writing
a
program
to
print
next
prime
number
to
the
given
prime
number

#Writing a prgm to find the nearest prime number
# we need to find both next and before prime numbers and check which is nearest to given number.
# prime number => 2,3,5,7,11,13,17
# for n=14 ,the next prime number to 14 is 17
#the before prime number is 13
# so distance b/w 14 to 17 is 3,
# distance b/w 14 to 13 is 1 ,
# so before prime number is nearest.

def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
n=int(input())
ap=0 # after_prime or next prime
bp=0 # before prime
i=n+1 # For finding next prime
while True:
    if isprime(i):
        ap=i        #next prime ap=1 7
        break
    i+=1
i=n-1   # for before prime
while True:
    if isprime(i):
        bp=i        # before prime is 13
        break
    i-=1
ad=ap-n     # 17-14 = 3
bd=n-bp     # 14-13 = 1

if ad==bd: # 3==1 False
    print(ap,bp)
elif ad<bd:     # 3<1 true so nearest prime num is before prime number that is 13
    print(bp)
else:
    print(ap)
