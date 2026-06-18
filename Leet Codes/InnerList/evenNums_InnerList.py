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
        if l[i][j]%2==0:
            print(l[i][j],end=" ")