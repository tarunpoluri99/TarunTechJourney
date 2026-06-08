'''
Valid Palindrome:

Simple Explanation
A word that reads the same forwards and backwards.
"racecar"
forwards  → r a c e c a r
backwards → r a c e c a r

Real Life Example
"A man, a plan, a canal: Panama"

Step 1 → lowercase everything
"a man, a plan, a canal: panama"

Step 2 → remove spaces, commas, colons -> "amanaplanacanalpanama"

Step 3 → reverse it -> "amanaplanacanalpanama"

Step 4 → compare "amanaplanacanalpanama" and "amanaplanacanalpanama"
      same! → true ✅

Approach
Step 1 → Convert to lowercase
Step 2 → Remove everything except letters and numbers
Step 3 → Reverse the cleaned string
Step 4 → Compare original cleaned vs reversed
         if same → true
         if different → false
'''
class A:
    def is_pal(self,s):
        s=s.lower()
        clean=""
        for i in s:
            if i.isalnum():
                clean+=i
        rev=clean[::-1]
        return rev==clean
s=input()
a=A()
if a.is_pal(s):
    print("True, Palindrome")
else:
    print("False, Not Palindrome")
