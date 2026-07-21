def uniquepaths(r,c):
    if r==0 and c==0:
        return 1
    if r<0 or c<0:
        return 0
    left=uniquepaths(r,c-1)
    top=uniquepaths(r-1,c)
    return left+top

def pathscount(n,m):
    return uniquepaths(n-1,m-1)