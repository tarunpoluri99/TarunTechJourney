'''
Maximum SubArray:
If your current partnership is negative
→ better to start a new partnership!

If your current partnership is positive
→ keep going, it's helping your total!

Approach:
Step 1 → Start with first element as both current_sum and max_sum
Step 2 → For each next element, ask:
         "current_sum + num"  → extend
         "num alone"          → start fresh
         Pick whichever is BIGGER
Step 3 → Update max_sum if current_sum
         is the best we've seen so far
Step 4 → Return max_sum at the end
Ex:

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

start → current = -2, max = -2

num=1  → max(-2+1, 1) = max(-1, 1) = 1   ← fresh start!
          max = 1

num=-3 → max(1+(-3), -3) = max(-2,-3) = -2 ← extend
          max = 1

num=4  → max(-2+4, 4) = max(2, 4) = 4   ← fresh start!
          max = 4

num=-1 → max(4+(-1),-1) = max(3,-1) = 3 ← extend
          max = 4

num=2  → max(3+2, 2) = max(5, 2) = 5    ← extend
          max = 5

num=1  → max(5+1, 1) = max(6, 1) = 6    ← extend
          max = 6 ✅

num=-5 → max(6+(-5),-5) = max(1,-5) = 1 ← extend
          max = 6

num=4  → max(1+4, 4) = max(5, 4) = 5    ← extend
          max = 6

Answer → 6 ✅  (subarray = [4,-1,2,1])
'''
class Solution:
    def max_SubArray(self,nums):
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(current_sum+num,num)
            max_sum=max(current_sum,num)
        return max_sum
nums=list(map(int,input().split()))
s1=Solution()
print(s1.max_SubArray(nums))