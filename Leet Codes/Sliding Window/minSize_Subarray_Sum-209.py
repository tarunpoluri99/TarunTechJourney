
def minSubArrayLen(k, a):
    l=0
    r=0
    sum=0
    minlen=float("inf")
    while r<len(a):
        sum+=a[r]
        while sum>=k:
            minlen=min(minlen,r-l+1)
            sum-=a[l]
            l+=1
        r+=1
    if minlen==float("inf"):
        minlen=0
    return minlen
l=list(map(int,input().split()))
k=int(input())
print(minSubArrayLen(k,l))
'''
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Rule:
 sum < target
      ↓
Expand the window (r++)

sum >= target
      ↓
Update answer
Shrink the window (l++)

Tip:
Expand until the condition becomes true. 
Once it becomes true, shrink as much as possible while keeping it true. 
Repeat until the end.
'''