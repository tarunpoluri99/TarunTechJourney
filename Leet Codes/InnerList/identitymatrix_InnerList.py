'''
Input:
3 -> row size
columns values:
    1 0 0
    0 1 0
    0 0 1
-> Identity Matrix
'''

# r=int(input())
# l=[]
# dc=True
# oc=True
# for _ in range(r):
#     l.append(list(map(int,input().split())))
# for i in range(len(l)):
#     for j in range(0,len(l[i])):
#         if i==j:
#             if l[i][j]!=1:
#                 dc=False
#         elif i!=j:
#             if l[i][j]!=0:
#                 oc=False
# if dc and oc:
#     print("Identity Matrix")
# else:
#     print("Not a Identity Matrix")


# Optimal:

r = int(input())
l = []
identity=True
for _ in range(r):
    l.append(list(map(int, input().split())))
for i in range(len(l)):
    if len(l[i])!=r:
        identity=False
        break

    for j in range(0, len(l[i])):
        if i==j and l[i][j]!=1:
            identity=False
        elif i!=j and l[i][j]!=0:
            identity=False

if identity:
    print("Identity Matrix")
else:
    print("Not a Identity Matrix")

'''
Identity Matrix:

-> rows and columns must be same size -> len(l[i])==r
-> The diagonal elements must be 1    -> i==j and l[i][j]==1
-> non diagonal elements must be 0    -> i!=j and l[i][j]==0

'''


