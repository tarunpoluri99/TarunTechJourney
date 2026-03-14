s=int(input())
e=int(input())

for i in range(s,e+1):
    fc=0
    c=0
    for j in range(1,i+1):
        if i%j==0:
            fc+=1
    if fc==2:
        print(i,"Prime",end=", ")
        c=c+1
if c%2==0:
    print(i)


