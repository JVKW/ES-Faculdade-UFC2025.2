def funcao(vetA, vetB):
    vetC = []
    for i in range(0, len(vetA)*2):
        if i % 2 == 0:
            vetC.append(vetA[i//2])
        else:
            vetC.append(vetB[i//2])

    return vetC

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)