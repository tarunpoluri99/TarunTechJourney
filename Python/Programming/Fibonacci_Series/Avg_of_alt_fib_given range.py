s=int(input())
e=int(input())
a,b=0,1
sum=0
ac=0
co=0
while a<=e:
    if a>=s:
        co+=1
        if co%2==1:
            ac+=1
            sum+=a

    c=a+b
    a=b
    b=c
if ac==0:
    print("No Fib")
else:
    avg=sum/ac
    print(f"{avg:.2f}")

