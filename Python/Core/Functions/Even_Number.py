def is_even(n):
        if n%2==0:
            return True
        else:
            return False
s=int(input())
e=int(input())
for i in range(s,e+1):
    res = is_even(i)
    if res:
        print(f"{i} is even")
    # else:
    #     print(f"{i} is odd") for odd
