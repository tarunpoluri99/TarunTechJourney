a=int(input())
b=int(input())
c=int(input())

# if a<=0 and (b>0 and c>0):
#     print("Invalid First Input")
# elif b<=0 and (a>0 and c>0):
#     print("Invalid Second Input")
# elif c<=0 and (b>0 and a>0):
#     print("Invalid third Input")
# elif a<=0 or (b<=0 or c<=0):
#     print("Sorry! Invalid Inputs")
# else:
#     h=max(a,b,c)
#     i=h
#     while i>0:
#         if i%a==0 and i%b==0 and i%c==0:
#             print(i,end=" ")
#             break
#         i+=i


if (a<=0 and b<=0) or (a<=0 and c<=0) or (b<=0 and c<=0):
    print("Sorry Invalid Inputs!")
elif a<=0 and (b>0 and c>0):
    print("Invalid First Input")
elif b<=0 and (a>0 and c>0):
    print("Invalid Second Input")
elif c<=0 and (a>0 and b>0):
    print("Invalid Third Input")
else:
    h=max(a,b,c)
    while True:
        if h%a==0 and h%b==0 and h%c==0:
            print(h,end=" ")
            break
        h+=1