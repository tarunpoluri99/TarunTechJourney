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
