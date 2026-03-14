n=int(input()) # 4
fact=1 # initial is 1 bcuz every num has 1 has its factorial
c=0
for i in range(1,n+1): # factorial form 1 to n
        fact*=i  # i values=> 1,2,3,4 => fact values =>1*1*2*3*4=>24
        c=c+1
        if c!=1:
            print("*",end=" ")
        print(i,end=" ")
print(f" = {fact}.",end="") # 4!=> 1*2*3*4