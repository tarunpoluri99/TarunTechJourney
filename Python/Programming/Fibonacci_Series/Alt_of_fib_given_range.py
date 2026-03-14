# Fibonacci Series in between given range
# if s = 13 and e=91 => f.series => 13 ,21,34,55,89

s=int(input())
e=int(input())
a,b=0,1
sum=0
ac=0
co=0
while a<=e:
    if a>=s:
        co+=1
        if co%2==1:
            print(a,end=" ")
    c=a+b
    a=b
    b=c
if co==0:
    print("No Fib")


# for i in range(s,e+1):
#     co+=1
#     if a>=s and a<=e:
#         print(a,end=" ")
#
#     c=a+b
#     a=b
#     b=c