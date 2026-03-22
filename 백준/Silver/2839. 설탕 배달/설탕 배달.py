N = int(input())
count = 0
while N > 0:
    if N%5 == 0:
        count+=N//5
        N%=5
    elif N >= 3:
        count+=1
        N-=3
    else:
        print(-1)
        break
if N == 0:
    print(count)