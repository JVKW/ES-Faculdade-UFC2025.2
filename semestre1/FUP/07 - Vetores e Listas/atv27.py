def funcao(lista):
    vetor = []
    for i in lista:
        if i != 0:
            vetor.append(i)
    
    return vetor

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)