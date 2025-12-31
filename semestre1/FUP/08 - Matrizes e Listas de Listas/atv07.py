def funcao(m, n):
    matriz = []

    for linha in range(m):
        matriz.append([])
        for coluna in range(n):
            if linha < coluna:
                matriz[linha].append(2 * linha + 7 * coluna - 2)
            elif linha == coluna:
                matriz[linha].append(3 * linha ** 2 - 1)
            elif linha > coluna:
                matriz[linha].append(4 * linha ** 3 - 5 * coluna ** 2 + 1)

    return matriz

def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print("")
x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
imprime(y)