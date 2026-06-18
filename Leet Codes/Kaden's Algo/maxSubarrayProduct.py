def maxSubarrayProd(a):
    pr=1
    mpr=float("-inf")
    su=1
    msu=float("-inf")
    for i in range(0,len(a)):
        pr*=a[i]
        mpr=max(pr,mpr)
        if pr==0:
            pr=1
        su*=a[len(a)-i-1]
        msu=max(su,msu)
        if su==0:
            su=1
    return max(mpr,msu)

# l=[3,2,-4,-1,0,-2,-4,-5,3]
l=[2,3,-2,4]
maxProduct=maxSubarrayProd(l)
print(maxProduct)


'''
-> Product behaves differently from sum.
-> A negative number can turn a small negative product into a large positive product.
-> So checking only from left → right is not enough.
-> We check both left → right and right → left.

-> Take prefix product for left to right
-> Take suffix product for right to left

'''
