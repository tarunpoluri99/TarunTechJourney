s = input()
indices = list(map(int, input().split()))

ans = [""] * len(s)

for i in range(len(s)):
    ans[indices[i]] = s[i]

print("".join(ans))
'''
ex:
s=bac
l=102

o/p: abc

'''