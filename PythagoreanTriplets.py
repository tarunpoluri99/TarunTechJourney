def sq(n):
    return n*n
l=list(map(int,input().split()))
res=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if sq(l[i])+sq(l[j])==sq(l[k]):
                print(f"{l[i]}*{l[i]} + {l[j]}*{l[j]}= {l[k]}*{l[k]}")
                res.append((i,j,k))
if res==[]:
    print("-1")
'''
Input 1 : 3 4 1 6 5

Output 1 : 3*3 + 4*4 = 5*5

Explanation : 
    3*3 + 4*4 != 1*1

    3*3 + 4*4 != 6*6

    3*3 + 4*4 = 5*5  True

    4*4 + 1*1 != 6*6

    4*4 + 1*1 != 5*5

    1*1 + 6*6 != 5*5

In the above explanation,
We have one combination which satifies the Pythagorean Triplet i.e., [3,4,5] '''