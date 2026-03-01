length_matrix = [
    [],
    [],
    [],
    [],
    [],
    [],
    [], 
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
for x in range(5):
    N=input()
    word = [s for s in N]
    for y in range(len(N)):
        length_matrix[y].append(word[y])

for mat in range(15):
    print(''.join(length_matrix[mat]), end='')