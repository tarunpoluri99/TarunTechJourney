def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2

r=int(input())
c=int(input())
l=[]
for _ in range(r):
    re=[]
    for _ in range(c):
        ele=int(input())
        re.append(ele)
    l.append(re)
for i in range(len(l)):
    for j in range(0,len(l[i])):
        if isprime(l[i][j]):
            print(l[i][j],end=" ")