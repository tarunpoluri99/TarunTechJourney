
def minSubArrayLen(a,k):
    l=0
    r=0
    total=0
    mlen=float("inf")
    while r<len(a):
        total+=a[r]
        while total>=k:
            mlen=min(mlen,r-l+1)
            total-=a[l]
            l+=1
        r+=1
    if mlen==float("inf"):
        mlen=0
    return mlen
a=[2,3,1,2,4,3]
k=7
print(minSubArrayLen(a,k))