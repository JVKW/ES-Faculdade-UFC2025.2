import random

def funcao(in_seed, n):
    matriz = []

    random.seed(in_seed)

    for linha in range(n):
        matriz.append([])
        for _ in range(n):
            matriz[linha].append(random.randint(1, 20))

    matrizTriangularInferior = []
    for linha in range(n):
        matrizTriangularInferior.append(matriz[linha][:])

    for linha in range(n):
        for coluna in range(linha + 1, n):
            matrizTriangularInferior[linha][coluna] = 0

    return matriz, matrizTriangularInferior

def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print("")
x1 = int(input(""))
x2 = int(input(""))
y1,y2 = funcao(x1,x2)
imprime(y1)
print("")
imprime(y2)