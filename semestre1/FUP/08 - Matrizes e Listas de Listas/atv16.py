def funcao(matriz):
    result = []

    for linha in range(len(matriz)):
        result.append([])

        maior = matriz[linha][0]
        if maior < 0:
            maior = maior * -1

        for n in range(1, len(matriz[0])):
            atual = matriz[linha][n]
            if atual < 0:
                atual = atual * -1

            if atual > maior:
                maior = atual

        for coluna in range(len(matriz[0])):
            result[linha].append(matriz[linha][coluna] / maior)

    return result

def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]:.2f} ", end="")
        print("")
def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat
mat = le(12, 13)
y = funcao(mat)
imprime(y)