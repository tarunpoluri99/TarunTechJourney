def is_prime(n):
    fc=0        #factorial Count
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False

s=int(input())
e=int(input())

if s>0 and e>0:
    sum=pc=ac=0     #pc=> Prime count and ac => Alternate Prime num count
    for i in range(s,e+1):
        b=is_prime(i)
        if b==True:
            pc=pc+1 # prime nums-> 11 13 17 19 23 29

            if pc%2==1: # Alt of Prime nums-> 11 17 23
                ac+=1
                sum+=i
    if sum==0:
        print("No prime Numbers")
    else:
        print(sum)
else:
    print("Invalid Range")