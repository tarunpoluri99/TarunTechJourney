n=int(input()) # 123
sum=0   # for sum initial value is 0
mul=1   #for mul initial value is 1 bcuz of if we put 0 anything mul with 0 is 0
t=n
while t>0:
    r=t%10 # r values -> 3 2 1
    mul*=r # mul= 1*3*2*1 => 6
    sum=sum+r # sum = 0+3+2+1 => 6
    t=t//10

# if add of digits is equal to product of digits then it's spy num
if sum==mul:
    print(f"{n} is a spy number")
else:
    print("Not a spy number")