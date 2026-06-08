'''
Contain Duplicates:

Check if any number appears more than once in a list.
[1, 2, 3, 1] → true  (1 repeats)
[1, 2, 3, 4] → false (all unique)

Approach:
Step 1 → Count how many times each number appears, store it in a dictionary

Step 2 → Loop through dictionary, if any number has count >= 2
       → return True (duplicate found!)

Step 3 → If loop finishes with no duplicates
         → return False
Ex:
nums = [1, 2, 3, 1]
After counting:
{1: 2, 2: 1, 3: 1}
 ↑
 1 appears twice → return True ✅

'''
class Solution():
    def iscontainsDuplicates(self,nums):
        count_nums={}
        for i in nums:
            if i in count_nums:
                count_nums[i]+=1
            else:
                count_nums[i]=1
        for i in count_nums:
            if count_nums[i]>=2: #Count_nums[i] gives pairs /values in the dict-> 2,1,3
                return True      # i -> Gives keys-> a,b,c
        return False
nums=list(map(int,input().split()))
s1=Solution()
if s1.iscontainsDuplicates(nums):
    print("true, It contains duplicates values")
else:
    print("false, It doesn't contains duplicate values")