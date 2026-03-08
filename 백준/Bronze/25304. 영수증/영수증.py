X=int(input())
N=int(input())
c=0
for i in range(1, N+1):
    a,b= map(int, input().split())
    c=c+a*b
if X == c:
    print('Yes')
else:
    print('No')
