n,m = map(int, input().split())
if m - 45 >= 0:
    print(n ,m-45)
else:
    if n == 0:
        print(23, 60+(m-45))
    else:
        print(n-1,60+(m-45))
    