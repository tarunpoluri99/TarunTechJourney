'''nums = [1,12,-5,-6,50,3]
           |1,12,-5,-6|   sum = 2

Slide →
nums = [1,12,-5,-6,50,3]
            |12,-5,-6,50| sum = 51

Slide →
nums = [1,12,-5,-6,50,3]
               |-5,-6,50,3| sum = 42

Maximum Sum = 51

Average = 51/4 = 12.75000
'''

def findMaxAverage(nums, k):
    winSum = sum(nums[:k])
    maxSum = winSum
    for i in range(k, len(nums)):
        winSum += nums[i]
        winSum -= nums[i - k]
        maxSum = max(maxSum,winSum)
    return float(maxSum)/k

l =list(map(int,input().split()))
k = 4
print(findMaxAverage(l, k))

