l=[3,2,-1,4,3,-20,6,4,15,-3,10]
# l=[-1]
s=0
m=float("-inf")
for i in range(len(l)):
    s+=l[i]
    if s>m:
        m=s
    if s<0:
        s=0
print(m)