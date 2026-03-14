def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False

s=int(input())  #10
e=int(input())  #30
if s>0 and e>0:
    sum=pc=ac=avg=0
    for i in range(s,e+1):
        if is_prime(i)==True:   #prime nums -> 11 13 17 19 23 29 #pc=6
            pc=pc+1

            if pc%2==1: # Alt prime nums -> 11 17 23 #ac=3
                sum+=i
                ac=ac+1
    if sum==0:
        print("No Prime Nums")
    else:
        avg=sum/ac
        print(f"{avg:.3f}") # for required decimal points here we need 3 points so .3f
else:
    print("Invalid Range")

