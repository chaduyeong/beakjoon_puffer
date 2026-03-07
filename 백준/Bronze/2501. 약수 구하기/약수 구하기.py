N,K = map(int, input().split())
factor = []
for X in range(1, N+1):
    if N%X == 0 :
        factor.append(X)

if len(factor) < K:
    print(0)
else:
    print(factor[K-1])