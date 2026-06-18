'''
Insertion Sorting

-> Swapping and no.of swappings are less
-> Less usage compartive to other sorting
'''

def insertionSort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j-1]>l[j]:
                l[j],l[j-1]=l[j-1],l[j]
            else:
                break

l=list(map(int,input().split()))
insertionSort(l)
print(l)

