n=int(input()) #18

if n<0: # if i/p is 18 doesn't execute this statement ..if i/p is -10 or -18 then executes
    n=-n # Converts negative input value into positive value
b=False
for i in range(1,n+1):
    if n%i==0:
        fc=0    #factor count ,we initialised it 0 because we need to find prime factors
        # print(i,end=" ")  # 1 2 3 6 9 18
        for j in range(1,i+1):
            if i%j==0:
                fc=fc+1 #counts the factors of every i value => i values=> 1 2 3 6 9 18

        if fc==2:   # only 2 and 3 has 2 factor count
            print(i,end=" ")
            b=True # changes True only if there are prime Factors
if b==False:
    print("No Prime factors")
