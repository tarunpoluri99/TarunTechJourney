#Finding the given year is leap year or not
# if n is divisible by 4 and not divisible by 100 then it's a Leap Year
# if n is divisible by 100, and also it should be divisible by 400 => Leap Year
# if this 2 conditions not satisfied then Not a Leap Year


def isleap(n):
    if n%4==0 and n%100!=0:
        return True
    elif n%100==0 and n%400==0:
        return True
    else:
        return False
n=int(input())
if isleap(n):
    print(f"{n} is Leap year")
else:
    print(f"{n} is not a Leap Year")
