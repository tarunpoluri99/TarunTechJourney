n=int(input())  #18
if n>0:
    for i in range(1,n+1):
        if n%i==0:  #cond for finding factors of n
            print(i,end=" ")    # 1 2 3 6 9 18
else:
    print("Invalid Input")