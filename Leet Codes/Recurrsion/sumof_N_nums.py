def sumofnat(n):
    if n==0:
        return 0
    return n+sumofnat(n-1)
n=int(input())
print(sumofnat(n))

'''

Sum of n Numbers using Recursion

sum of 5 Nums => 1+2+3+4+5 = 15
sum of 3 Nums => 1+2+3 =6

ex:
n=3
print(sumofnat(3))  => sumofnat(3) = 6
    ||
    n=3
    return 3+sumofnat(2)    => 3+3=6
            ||
            n=2
            return 2+sumofnat(1)    => 2+1=3
                ||
                n=1
                return 1+sumofnat(0) => 1+0=1
                    ||
                    n=0
                    if n==0 :
                    return 0 

'''