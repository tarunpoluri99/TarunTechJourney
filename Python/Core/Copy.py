'''
Copy:
-> 1.Shallow copy
-> 2.Deep copy
'''
# Shallow Copy:
l1=[1,2,3,4,5]
n=l1.copy()


#Deep copy
import copy
l=[10,20,30,40,[20,30]]
s=l.copy()
j=copy.deepcopy(l)
s[3]=30
s[4][0]=60
print(j)
print(l)
print(s)