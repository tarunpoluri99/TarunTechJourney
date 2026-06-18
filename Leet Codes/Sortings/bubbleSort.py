'''
-> Same as linear Sorting
-> It iterates f

'''
def bubbleSort(l):
    c=0
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=list(map(int,input().split()))
bubbleSort(l)
print(l)