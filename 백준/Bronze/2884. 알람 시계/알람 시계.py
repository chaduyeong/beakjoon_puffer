n,m = map(int, input().split())
if m - 45 >= 0:
    m=m-45
else:
    n=n-1
    m=m+15
    if n < 0:
        n= 23
print(n,m)
    