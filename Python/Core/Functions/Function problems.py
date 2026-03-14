'''
#program to check num is even or odd
def fun(a):
    if a%2==1:
        return "odd"
    return "even"
x=fun(8)
print(x)
'''

'''
#Write a function that takes a number and returns its square.

def fun(a):
    return a**2
x=fun(8)
print(x)
'''
'''
# Write a function that takes two numbers and returns their sum
def fun(a,b):
    return a+b
x=fun(10,20)
print(x)

'''
'''
#Write a function that takes a string and returns its length (without using len()).
def fun(a):
    c=0
    for i in a:
        c+=1
    return c
print(fun("Hii"))
'''
'''
#Write a function to find the largest of three numbers.
def big(a,b,c):
    if a>b and a>c:
        return "a is big"
    elif b>a and b>c:
        return "b is big"
    else:
        return "c is big"

print(big(60,100,30))
'''
'''
#Write a function to calculate factorial of a number.
Factorial:
Factorial of a number n means multiplying all positive numbers from n down to 1.
Example:
5! = 5 × 4 × 3 × 2 × 1
Also remember:
0! = 1 (This is a rule in mathematics)'''
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
'''
'''
#Write a function that takes a number and returns reverse of that number
def rev(a):
    rev=0
    while a>0:
        c=a%10
        rev=rev*10+c
        a=a//10
    return rev
print(rev(101))
'''
'''
#Write a function to check whether a number is a prime number.
def prime(a):
    if a <= 1:
        return "Not Prime"
    else:
        for i in range(2, a):
            if a % i == 0:
                return "Not Prime"
        return "Prime"

print(prime(2))
'''