a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
j=0
res=[]

#  For comparing the Two Lists Using Pointers

while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1

# For remaining Elements in the Lists
while i<len(a):
    res.append(a[i])
    i+=1
while j<len(b):
    res.append(b[j])
    j+=1

print(res)

'''
Sorted Lists

a = [1, 4, 7, 10]
b = [2, 3, 8, 9]

#pointers
i = 0
j = 0
ans = []

Tracing:

1 vs 2  → add 1   → i = 1
4 vs 2  → add 2   → j = 1
4 vs 3  → add 3   → j = 2
4 vs 8  → add 4   → i = 2
7 vs 8  → add 7   → i = 3
10 vs 8 → add 8   → j = 3
10 vs 9 → add 9   → j = 4

i = 3 and j = 4

Remaining element in list a is 10 so for that

while i< len(a): => 3 < len(a) => 3< 4 True
    res.append(a[3]) => 10
    i+=1
    4<4 : False

'''
