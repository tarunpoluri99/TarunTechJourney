def fun(a):
    if d[a]>50:
        return True
    return False
    return a>50
d={"apple":100,"banana":40,"cherry":150}

result=list(filter(fun,d))
print(result)