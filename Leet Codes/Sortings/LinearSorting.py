'''
General Sorting/Linear Sorting:

-> Used to normal sort the dataset
-> fixed at i and checks j values at every index
-> Bigger Time complexity

ex:
l=[7,9,1,4,2,5]

i=0 => j=1 -> 9 7>9
       j=2 -> 1 7>7 T =>
       j=3 ->
       j=4 ->
       j=5 ->
i=1,2,3,4
like that in every index it checks j values upto n

'''

def linearSort(l):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]

l=list(map(int,input().split()))
linearSort(l)
print(l)