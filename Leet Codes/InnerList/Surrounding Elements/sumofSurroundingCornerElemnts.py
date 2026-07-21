'''
Corner elements: TOp Left, Top Right , Bottom Left,Bottom Right

              Element Accessing         Conditions
Top Left:       a[i-1][j-1]         i-1>=0 and j-1>=0:
Top Right:      a[i-1][j+1]         i-1>=0 and j+1<c
Bottom Left:    a[i+1][j-1]         i+1<r and j-1>=0
Bottom Right:   a[i+!][j+1]         i+1<r and j+1<c

3,2,4,9
5,6,1,2
4,3,6,1

'''
a=[[3,2,4,9],[5,6,1,2],[4,3,6,1]]
r=3
c=4
for i in range(0,r):
    for j in range(0,c):
        s=0
        if i-1>=0 and j-1>=0:
            s+=a[i-1][j-1]
        if i-1>=0 and j+1<c:
            s+=a[i-1][j+1]
        if i+1<r and j-1>=0:
            s+=a[i+1][j-1]
        if i+1<r and j+1<c:
            s+=a[i+1][j+1]
        print(f"{a[i][j]} : {s}")