N,M = map(int,input().split())
A_matrix = []
B_matrix = []

for _ in range(N):
    A_matrix.append(list(map(int,input().split())))
for _ in range(N):
    B_matrix.append(list(map(int,input().split())))

for X in range(N):
    for Y in range(M):
        print(A_matrix[X][Y] + B_matrix[X][Y], end=' ')
    print()