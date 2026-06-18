def selectionSort(l):
    max_in=0
    for i in range(0,len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[max_in]:
                max_in=j
            l[max_in],l[len(l)-i-1]=l[len(l)-i-1],l[max_in]

l=list(map(int,input().split()))
selectionSort(l)
print(l)
