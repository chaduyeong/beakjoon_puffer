N=int(input())
count = 0
for _ in range(N):
    word = input()
    seen = set()
    group = True 
    for x in range(0,len(word)-1):
        if word[x] == word[x+1]:
            if word[x] not in seen:
                seen.add(word[x])
        elif word[x] != word[x+1]:
            if word[x] not in seen:
                seen.add(word[x])
            if word[x+1] in seen:
                group = False
                break
    if group==True:
        count += 1            
print(count)
                