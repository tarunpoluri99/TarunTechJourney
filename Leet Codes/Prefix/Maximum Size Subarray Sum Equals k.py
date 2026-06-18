class Solution(object):
    def MaxsubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        psum=0
        pre={0: -1}
        max_len=0
        for i in range(len(nums)):
            psum+=nums[i]
            if (psum - k) in pre:
                max_len = max(max_len, i - pre[psum - k])

            if psum not in pre:  # store first occurrence only
                pre[psum] = i
        return max_len-1
s=Solution()
l=[3,2,1,1,-1,2,-4,5,1,3]
k=4
print(s.MaxsubarraySum(l,k))

'''
For every index:

1.Calculate prefix sum.
2.Compute:
    need = prefix_sum - k

3.If need exists in hashmap:
    length = current_index - first_index_of_need
4.Update maximum length.
5.Store current prefix sum only if it is seen for the first time.

That's the entire logic behind the maximum-length version.

Ex:
nums = [1, -1, 5, -2, 3]
k = 3

| Index | Value | Prefix Sum |
| ----- | ----- | ---------- |
| 0     | 1     | 1          |
| 1     | -1    | 0          |
| 2     | 5     | 5          |
| 3     | -2    | 3          |
| 4     | 3     | 6          |


-> At index 3:
    prefix sum = 3 => 1 + (-1) + 5 + (-2) = 3
    
-> current prefix sum = psum
-> Which previous prefix sum should exist?
    Formula:
        subarray sum = current_prefix - previous_prefix
     => k = current_prefix - previous_prefix
     => previous_prefix = current_prefix - k

'''
