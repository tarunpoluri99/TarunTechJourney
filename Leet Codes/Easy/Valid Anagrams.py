'''
Anagrams:
Two words are anagrams if they use the exact same letters, same count, different order.
"cat" → "act"  ✅ here  {c=1,a=1,t=1} same letters,count and may be different order.
"listen" → "silent"  ✅
"cat" → "car"  ❌  (different letters)

Approach:

Step 1 → If lengths differ → return False immediately
Step 2 → Count how many times each letter appears in s
Step 3 → Count how many times each letter appears in t
Step 4 → If both counts match → True, else → False
'''
class Solution:
    def isAnagrams(self, s: str, t: str):
        count_s={}
        count_t={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in count_s:
                count_s[i]+=1
            else:
                count_s[i]=1
        for i in t:
            if i in count_t:
                count_t[i]+=1
            else:
                count_t[i]=1
        return count_s==count_t
s=input()
t=input()
s1=Solution()
if s1.isAnagrams(s,t):
    print("true")
else:
    print("false")