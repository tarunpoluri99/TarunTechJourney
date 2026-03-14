def is_prime(n):
    fc=0        #fc=> Factorial counts
    for i in range(1,n+1):
        if n%i==0:      # cond for finding factors n
            fc=fc+1
    if fc==2:       # A Prime nums only 2 factors 1 and itself
        return True
    else:
        return False
s=int(input())
res=is_prime(s)
if res==True:
    print(f"{s}  is prime")
else:
    print("Not a prime")