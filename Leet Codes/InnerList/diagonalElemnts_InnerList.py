r=int(input())
l=[]
for _ in range(r):
    l.append(list(map(int,input().split())))
for i in range(len(l)):
    for j in range(0,len(l[i])):
        if i==j:
            print(l[i][j],end=" ")