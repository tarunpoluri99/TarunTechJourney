def sumofDigit(n):
    if n==0:
        return 0
    return n%10+sumofDigit(n//10)
n=int(input())
print(sumofDigit(n))
'''
Sum of Digits

ex:
198 => 1+9+8

In recursion :

n=198
n%10 + sum_of_Digit(n//10) 

=> remainder +sum of Remaining Digits

8 + sum_of_Digit(19) => 8 + 10 = 18
            ||
            n=19
            9 + sum_of_Digit(1) => 9 + 1 = 10
                        ||
                        n=1
                        1 + Sum_of_Digit(0) => 1 + 0 = 1
                                ||
                                n=0
                                return 0

'''