# Adding 5 to list using lambda
# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x+[5],l))
# print(k)
# print(l)
from functools import reduce

# d={"apple":100,"banana":40,"cherry":150}
# print(d.keys())
# print(d.values())
# print(d.items())
# f=dict(filter(lambda x:x[1]>50,d.items()))
# print(f)

# #split() function -> used to split the value
# k=input() #string value
# print(k.split("$")) #whenever $ split is used it seperate string into new element
# print(type(k)) #str i/p Hello$world o/p: 'Hello''World'

#Finding largest using map and reduce function
# k=list(map(int,input().split()))
# m=-10**6
# for i in k:
#     if m<i:
#         m=i
from functools import reduce
# print(reduce(lambda x,y: x if x>y else y,k))
#
# print(m)

#10th Question
l=[5,10,15,20,25,30]
# for squaring we used map()
sq=list(map(lambda x: x**2,l))  #[25,100,225,400,625,900]
print(sq)
# for divisible's of 5 we used filter() returns only when true

di=list(filter(lambda x: x%5==0,sq))#[25,100,225,400,625,900]

#adding those divisibles we use reduce()=>x=25,y=100=>x+y=125=>x=125,y=225=>x+y:350=>x...

v=reduce(lambda x,y:x+y,di)#2275

# writing in all code in single pipeline

v=reduce(lambda x,y :x+y,filter(lambda x:x%5==0,map(lambda x:x**2,l)))

print(v)