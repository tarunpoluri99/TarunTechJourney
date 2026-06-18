r=int(input())
c=int(input())
l=[]
for _ in range(r):
    re=[]
    for _ in range(c):
        ele=int(input())
        re.append(ele)
    l.append(re)
sum_list=[]
for i in range(len(l)):
    s=0
    for j in range(0,len(l[i])):
        s+=l[i][j]
    sum_list.append(s)
print(sum_list)