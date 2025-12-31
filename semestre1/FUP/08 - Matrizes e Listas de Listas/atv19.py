import random

def calcular_media(vetor):
    soma = 0
    tam = len(vetor)
    for i in range(tam):
        soma += vetor[i]
    
    media = soma / tam

    return media

def funcao(m, n, n_seed, inicio, fim):
    matriz = []
    vetor = []

    random.seed(n_seed)

    for i in range(m):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(inicio, fim))

    for linha in range(len(matriz)):
        if linha % 2 == 0:
            vetor.append(calcular_media(matriz[linha]))
        else:
            soma = 0
            for coluna in range(len(matriz[0])):
                if matriz[linha][coluna] < 0 and matriz[linha][coluna] % 3 == 0:
                    soma += 1
            vetor.append(soma)

    return matriz, vetor

def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print("")
x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
x4 = int(input(""))
x5 = int(input(""))
y1,y2 = funcao(x1,x2,x3,x4,x5)
imprime(y1)
print(y2)