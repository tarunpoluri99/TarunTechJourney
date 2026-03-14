class Prime():
    p=2
    while True:
        f=0
        for i in range(2,p/2):
            if p%i==0:
                f=1
                break
        if p>400:
            return None

        elif p==0:
            yield p
        else:
            p+=1
            continue
p=Prime()
print(next(p))
