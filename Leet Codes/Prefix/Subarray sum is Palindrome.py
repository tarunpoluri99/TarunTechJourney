''' This is Brute force Approach

def ispal(n):
    t=n
    rev=0
    while t>0:
        r=t%10
        rev=rev*10+r
        t=t//10
    return n==rev
def subsum(l):
    for i in range(len(l)):
        s=0
        for j in range(i,len(l)):
            s+=l[j]
            if ispal(s):
                return s
    return -1

l=[12,5,7,11]
print(subsum(l))
'''

'''
ex:

=> array [12, 5, 7, 11]. 
    
1. choose the starting index 0 and keep a running sum. 
2. Add 12, the sum becomes 12, check if 12 is a palindrome.
    It is not, so extend the subarray by adding the next element 5.
3. Now the sum becomes 17, check if 17 is a palindrome. 
    It is not, so add the next element 7. 
    The sum becomes 24, check again. Not a palindrome. 
    Add the next element 11, the sum becomes 35, check again. Not a palindrome.

4. Now all subarrays starting from index 0 have been checked, 
    so move the starting index to 1 and reset the sum to 0. 
    Add 5, the sum becomes 5. Check if 5 is a palindrome. 
    Since reversing 5 still gives 5, it is a palindrome, 
    so return 5 (or count it, depending on the question).

In general, start from every index one by one. 
For each starting index, keep extending the subarray towards the right and keep updating the sum. 
After every addition, check whether the current sum is a palindrome.
If it is, perform the required action (return it, count it, store it, etc.). 
Then continue until all possible subarrays have been checked.

'''
# This is Prefix approach
def ispal(n):
    t = abs(n)
    rev = 0
    while t > 0:
        rev = rev * 10 + t % 10
        t //= 10
    return abs(n) == rev

def palindrome_subarray_sum(nums):
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                s = prefix[j]
            else:
                s = prefix[j] - prefix[i - 1]

            if ispal(s):
                return s
    return -1

l = [12, 5, 7, 11]
print(palindrome_subarray_sum(l))

