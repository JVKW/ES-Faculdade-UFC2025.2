vetor = []
for i in range(10):
    val = int(input())
    vetor.append(val)

for x in range(10):
    for y in range(x+1, 10):
        if vetor[x] == vetor[y]:
            print(vetor[x])