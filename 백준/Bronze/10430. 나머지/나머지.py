a,b,c = map(int, input().split())
one=a+b
two=a%c
three=b%c
four=a*b
print(one%c)
print((two+three)%c)
print(four%c)
print((two*three)%c)