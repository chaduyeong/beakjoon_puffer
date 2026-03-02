num_dic = ['0','1','2','3','4','5','6','7','8','9']
dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17, 'I':18,
       'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,
       'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
total = 0
N,B = input().split()   # CD01 16 => 10DC 
B= int(B)
N=list(N)
N.reverse()
for a in range(len(N)):
    if N[a] in num_dic:     # if N[a].isdigit(): 를 이용하면 문자열에서 0~9가 아닌 수들은 알아서 false로 걸러준다.
       total += int(N[a])*(B**a)
    elif N[a] not in num_dic:
       total += dic[N[a]]*(B**a)
print(total)