def evenNums(s,e):
    if s>e:
        return
    if s%2==0:
        print(s,end=" ")
    evenNums(s+1,e)
s=int(input())
e=int(input())
evenNums(s,e)
'''
Even Nums

1 to 10 : 2 4 6 8 10

s=1
e=10
evenNums(1,10)
    ||
    s=1
    s%2==0 False
    evenNUms(s+1,e) => evenNums(2,10)
                            ||
                            s=2
                            2%2==0: True
                            print => 2
                            evenNums(3,10)
                                ||
                                s=3
                                3%2==0: False
                                evnNums(4,10)
                                    ||
                                    s=4
                                    4%2==0: True
                                    print => 4
                                    ....
                                    ...
                                    s=10
                                    10%2==0: True
                                    print => 10
                                    evenNums(11,10)
                                        s>e: True
                                        return
                                        
                                        
                                

'''