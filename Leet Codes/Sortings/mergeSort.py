# For conquer this merge method is used
def merge(a,b):
    i=0
    j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    while i<len(a):
        res.append(a[i])
        i+=1
    while j<len(b):
        res.append(b[j])
        j+=1
    return res

# For dividing the lists into multiple single element lists => sp method=> split
def sp(l):
    n=len(l)
    if n==1:
        return l
    mid=n//2
    left=sp(l[0:mid])
    right=sp(l[mid:n])
    return merge(left,right)


l=list(map(int,input().split()))
res=sp(l)
print(res)