'''
Tech Number checking:
1. take number and count its digits.
2. a. If the count is odd then not a Tech Number.
   b If the count is even then it continued the process
        then c=c/2
3. Now divide num into two halves
    -> for 1st half use n//100 convert into integer => x= int(n//(10**c))
    -> for 2nd half use n%100 convert into integer => y= int(n%(10**c))

4. Now add both half's s=>x+y
5. Square the sum value => rs=s*s
6. if the resultant value is equals to n => rs==n
    -> Then it is a Tech num... else not a tech num.
'''

n=int(input())  #i/p -> 2025
t=n
c=0
while t>0:
    r=t%10  # r->5 2 0 2
    c+=1    #c=4
    t=t//10
if c%2==1:      # if count is odd, then not a Tech Num
    print("Not a Tech Num")
else:
    c=c/2 # c=4/2 => c=2 now 10**c => 10**2    10*10= 100 so divide n with 100
    # if count is even,then it has a chance
    # then we need to divide num into 2 half's

    x=int(n//(10**c))# 2025=> 20 1st half
    y=int(n%(10**c))   #2025=> 25 2nd half
    s=int(x+y)      # add both half's => 20+25=45
    s=s*s           # Now square the sum value => 45*45= 2025
    if s==n:        # if n==s: => 2025 == 2025 :
        print("Tech Num") # tech num
    else:
        print("Not Tech Num")