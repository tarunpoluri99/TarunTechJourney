s=int(input())
e=int(input())

if s<e:
    for i in range(s,e+1):
        if i%2==0:
            print(f"{i} is even")
else:
    print("Invalid Range")

