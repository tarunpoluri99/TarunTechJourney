def isarm(n):
    t=n
    dc=0
    while t>0:
        dc+=1
        t=t//10
    t=n
    su=0
    while t>0:
        r=t%10
        su=su+pow(r,dc)
        t=t//10
    return su==n
s=int(input())
e=int(input())
s=abs(s)
e=abs(e)
sum_arm=0
if s==0 or e==0:
    print("Invalid Inputs")
else:
    if s>e:
        s,e=e,s
    for i in range(s,e+1):
        if isarm(i):
            sum_arm+=i
    if sum_arm==0:
        print("No Armstrong Numbers in the Given Values")
    else:
        print(sum_arm)

# 1
# 100
# sum_arm= 45
