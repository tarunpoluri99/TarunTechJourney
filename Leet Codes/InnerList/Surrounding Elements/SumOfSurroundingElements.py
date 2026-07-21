'''
Border Elements => Top,Bottom,Left,Right

Top:        a[i-1][j]       i-1>=0
Bottom:     a[i+1][j]       i+1<r
Left:       a[i][j-1]       j-1>=0
Right:      a[i][j+1]       j+1<c

'''

a=[[3,2,4,9],[5,6,1,2],[4,3,6,1]]
r=3
c=4
for i in range(0,r):
    for j in range(0,c):
        s=0
        if i-1>=0:
            s+=a[i-1][j]
        if i+1<r:
            s+=a[i+1][j]
        if j-1>=0:
            s+=a[i][j-1]
        if j+1<c:
            s+=a[i][j+1]
        print(f"{a[i][j]}:{s}")
