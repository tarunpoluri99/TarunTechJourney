# When row and column give and inputs are given one by one

# r=int(input())
# c=int(input())
# l=[]
# for _ in range(r):
#     re=[]
#     for _ in range(c):
#         ele=int(input())
#         re.append(ele)
#     l.append(re)
# print(l)
# # Accessing InnerList Elements
# for i in range(len(l)):
#     for j in range(0,len(l[i])):
#         print(l[i][j],end=" ")

# When row given and inputs are given side by size
r=int(input())
l=[]
for _ in range(r):
    l.append(list(map(int,input().split())))
print(l)
for i in range(len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end=" ")

'''
Type - 1:
2 => row size
3 => column size
elements:
    1
    2
    3
    4
    5
    6
l= [[1 2 3], [4 5 6]]
ele = 1 2 3 4 5 6


Type - 2:

2 => row size
column values 
    10 20 30
    20 50 50
l= [[10, 20, 30], [20, 50, 50]]
ele = 10 20 30 20 50 50 
'''