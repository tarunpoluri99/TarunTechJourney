def sumofFib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return sumofFib(n-1)+sumofFib(n-2)

n=int(input())
print(sumofFib(n))

'''
Sum of Fibnocaci Numbers

Fib series : 0 1 1 2 3 5 8 13 21 ...
!st Fib => 0
2nd Fib => 1
3rd Fib => 1
4th Fib => 2
5th Fib => 3

nth Fib = Sum(n-1)+Sum(n-2)
Fib Number = sum of previous 2 nums
'''
