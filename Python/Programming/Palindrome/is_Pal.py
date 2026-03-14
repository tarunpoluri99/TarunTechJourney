def is_Pal(n):
    rev=0
    t=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    return t==rev
n=int(input())
if n<0:
    print("Invalid Input")
else:
    b=is_Pal(n)
    if b==True:
        print("Palindrome Number")
    else:
        print("Not a Palindrome NUmber")