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
        b=is_prime(i)
        if b==True:
            pc=pc+1 #prime Nums->11 13 17 19 23 29 #pc=6
            sum+=i

    if sum==0:
        print("No Prime Nums")
    else:
        avg=sum/pc      # 51/6 =>18.666666 print(avg)=>18.66666
        # for required decimals => use r:.3f
        print(f"{avg:.3f}") # here 3f determines decimal points
else:
    print("Invalid Inputs")


