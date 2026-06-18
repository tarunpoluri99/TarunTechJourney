class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        psum=0
        c=0
        pre={}
        pre[0]=1
        for i in range(len(nums)):
            psum+=nums[i]
            ch=psum-k
            c=c+pre.get(ch,0)
            pre[psum]=pre.get(psum,0)+1
        return c
s=Solution()
l=[3,2,1,1,-1,2,-4,5,1,3]
k=4
print(s.subarraySum(l,k))


'''
=> At every index:
    need = prefix_sum - k
=>If need has appeared x times before,
 then there are x subarrays ending at the current index whose sum is k.
 
So:

1. Calculate prefix sum.
2. Find need = prefix_sum - k.
3. Add frequency of need to answer.
4. Store/update current prefix sum frequency.
5. Continue.

ex:
nums = [1,1,1]
k = 2
1.  prefix_sum = 0
    count = 0
    dict = {0:1}

2.At first element ,nums[0]=> 1
    prefix_sum - k
    = 1 - 2
    = -1
    Has -1 appeared before? No 
    So,Count=0
    dict= {0:1, 1:1}
    
3.At second elemnt => 1
    prefix_sum - k => 1+1 - 2 => 0
    Has 0 appered Before? Yes 
    So count =1
    dict = {0:1, 1:1, 2:1}

4.At Third element => 1
    prefix_sum - k => 1+1+1 - 2 => 1
    Has 1 appered Before? Yes
    So count =2
    dict ={0:1, 1:1, 2:1, 3:1}

5.Count=2
'''
