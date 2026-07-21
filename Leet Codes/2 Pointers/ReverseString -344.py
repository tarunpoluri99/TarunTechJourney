def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    #  Using 2 pointers
    l = 0
    r = len(s) - 1
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

    # Using Reversing

    # r=len(s)-1
    # rev=[]
    # while r>=0:
    #     rev.append(s[r])
    #     r-=1
    # return rev

    #  another method

    # rev=[]
    # for i in range(len(s)-1,-1,-1):
    #     rev.append(s[i])
    # return rev


s = ['h', 'e', 'l', 'l', 'o']
print(reverseString(s))

'''
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''