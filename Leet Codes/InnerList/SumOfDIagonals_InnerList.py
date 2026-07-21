'''
Diagonals:

00 01 02 03         Primary Diagonals => 00 11 22 33 => i==j
10 11 12 13
20 21 22 23         Secondary Diagonals => 03 12 21 30 => i+j=r-1
30 31 32 33                                            => j=r-i-1
'''
# r=int(input())
# l=[]
# for _ in range(r):
#     l.append(list(map(int,input().split())))
# s1=0
# s2=0
# id=True
# for i in range(len(l)):
#     if len(l[i])!=r:
#         id=False
#         break
#     for j in range(0,len(l[i])):
#         if i==j:
#             s1+=l[i][j]
#         if i==r-j-1:
#             s2+=l[i][j]
# if id:
#     print(s1,s2)


# Optimal:
r=int(input())
l=[]
for _ in range(r):
    l.append(list(map(int,input().split())))
s1=0
s2=0
for i in range(r):
    s1+=l[i][i]
    s2+=l[i][r-i-1]
print(s1,s2)

