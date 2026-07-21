
def twoSum(numbers,target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        cusum = numbers[i] + numbers[j]
        if cusum == target:
            return [i + 1, j + 1]
        elif cusum > target:
            j-= 1
        else:
            i+= 1
    return [-1, -1]

l=list(map(int,input().split()))
target=int(input())
print(twoSum(l,target))

'''
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. 
Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''