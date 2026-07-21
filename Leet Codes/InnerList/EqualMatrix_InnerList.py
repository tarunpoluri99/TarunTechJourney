r=int(input())
l=[]
for _ in range(r):
    l.append(list(map(int,input().split())))
c=0
# for i in range(0,r):
#     for j in range(0,c):
#         if l[i][0]!=l[i][j]:
#             c+=1
#             print("Not Equal Matrix")
#             break
#     if c!=0:
#         break
# if c==0:
#     print("Equal Matrix")
