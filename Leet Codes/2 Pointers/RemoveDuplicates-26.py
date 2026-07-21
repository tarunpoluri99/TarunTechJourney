
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
l=list(map(int,input().split()))
print(removeDuplicates(l))

'''
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: 
Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''