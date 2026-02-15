# a=23
# if a%2!=0:
#     b=a/2
#     print(b) #11.5

#2nd Question
# a=4
# for i in range(1,10):
#     if a>i:
#         print(i) # 1 2 3

#3rd Question
# a=2
# if a==1:
#     print(a*3)
# elif a==2:
#     print(a%a)
# elif a==3:
#     print(a/a) #o/p 0

#4th Question
# a=13
# b=12
# c=6
# d=(a+b)//c
# print(d)    #o/p 4

#5th Question
# n=10
# a=1
# b=2
# while a<=n:
#     print(a)
#     next=a+b
#     a=b
#     b=next  #o/p 1 2 3 5 8

#6th Question
# a,b=10,2
# print(a<<b)#40
# print(a>>b)#2

#7th Question
# a,b=34,11
# c=a
# a=b
# b=c
# print(a)
# print(b)
# print( c )    #o/p 11 34 34

#8th Question
# n,c=173,0
# while True:
#     n=n//10
#     c=c+1
#     if c==7:
#         break
# print(n)    #0

#9th Question
# ab=10
# ba=100
# if(ab//ba)==(ba%ab):
#     print(ab)
# else:
#     print(ba) # 10

#10th Question
# a=3
# b=4
# print(a>=b or a<b)          #True
# print((a/2)>b and a<(2*b))  # False

#11th Question
# n=100
# if n%10==0 or n<10:
#     n=n-1
#     if n%2==0:
#         print("Sad")
#     else:
#         print("Happy") #Happy
#     print(i)           # error (i) not defined

#12th Question
# for i in range(1,10):
#     if i%2==0:
#         continue
#     elif i==5:
#         print("Reached 5")
#     else:
#         print(i)        #o/p 1 3 Reached 5 7 9

#13th Question
# x=13
# while x<=8:
#     if x==3:
#         x=x+1
#         continue
#     elif x<5:
#         print("Small:",x)
#     else:
#         print("Large:",x)
#         x=x+1
# print(x)    #13

#14th Question
# k=20
# while k>=5:
#     k=k-3
#     if k>10:
#         print(k<<1)
#     else:
#         print(k>>1)

#15th Question
# a,b=5,34
# for i in range(1,6):
#     a=a+b
#     if a>10 and a<20:
#         print(a>>1)
#     elif a>-20:
#         print(a<<1)
#     else:
#         print(a^b) #78 146 214 282 350
