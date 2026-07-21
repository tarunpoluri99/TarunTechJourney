a=[[0,1,2],[10,11,12]]
b=[[0,1,2,3],[10,11,12,13],[20,21,22,21]]
r1=len(a)
c1=len(a[0])
r2=len(b)
c2=len(b[0])
res=[]
for i in range(0,r1):
    for j in range(0,c2):
        sum=0
        for k in range(0,c1 or r2):
            sum+=a[i][k]*b[k][j]
        print(sum,end=" ")
    print()
