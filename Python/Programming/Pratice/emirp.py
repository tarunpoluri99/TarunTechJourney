'''A number is Emirp number ,when the number is reversed and the reversed number is tprime
Then it's an Emirp Number
ex: n= 91 , rev(n)=> 19 => 19 is prime number then 91 is Emirp Number
'''

def is_Prime(n):  # n value
    fc=0
    for i in range(1,n+1): # i values 1 to n
        if n%i==0: # formula to find factors => n%i
            fc=fc+1  # factorial count
    if fc==2:       # if fc==2 -> prime
        return True
    else:           # fc!=2 -> not prime
        return False
n=int(input())  #91
rev=0       #rev=0
t=n
while t>0:
    r=t%10 #r->1 9
    rev=rev*10+r   # rev = 19
    t=t//10
m=rev           # rev=19
print(f"rev is {m}")
b=is_Prime(m)
if b==True: # if m is prime then Emirp number
    print(f"{n} is Emirp number")
else:
    print("Not a Emirp Number")
