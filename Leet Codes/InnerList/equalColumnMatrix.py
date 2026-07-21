'''
Column wise transversal:

'''
from numpy.ma.extras import column_stack

# r=3
# c=4
# l=[[00,1,2,3],[10,11,12,13],[20,21,22,23]]
# for i in range(0,c):
#     for j in range(0,r):
#         print(l[j][i])

''' Equal Column wise matrix:
        columns
        c1
rows    1  2  1
        1  2  1
        1  2  1
'''
r=3
c=3
a=[[1,2,1],[1,2,1],[1,2,1]]
ic=0
for i in range(0,c):
    for j in range(0,r):
        if a[0][i]!=a[j][i]:
            ic+=1
            print("Not a Column Matrix")
            break
    if ic!=0:
        break
if ic==0:
    print("Equal Matrix")