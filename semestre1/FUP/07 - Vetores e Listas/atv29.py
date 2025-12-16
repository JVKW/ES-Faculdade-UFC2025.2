def funcao(list):
    vetor = list
    num_vetor = len(vetor)

    for i in range(num_vetor-1):
        quebra = False
        for j in range((num_vetor - i)-1):
            if list[j] < list[j+1]:
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
                quebra = True
        if not quebra:
            break

    return vetor

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)