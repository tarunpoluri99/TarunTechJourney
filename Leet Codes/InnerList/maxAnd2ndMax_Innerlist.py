'''
Finding max and second max in the given Inner List
'''
r=int(input())
c=int(input())
l=[]
m1=float("-inf")
m2=float("-inf")

for _ in range(r):
    re=[]
    for _ in range(c):
        ele=int(input())
        re.append(ele)
    l.append(re)

for i in range(len(l)):
    for j in range(0,len(l[i])):
        if l[i][j]>m1:
            m2=m1
            m1=l[i][j]
        elif l[i][j]<m1 and l[i][j]>m2:
            m2=l[i][j]
print(m1,m2,end=" ")

