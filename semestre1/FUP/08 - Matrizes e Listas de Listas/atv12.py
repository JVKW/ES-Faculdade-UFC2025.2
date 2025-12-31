def funcao(matriz):
    retorno = []

    for coluna in range(len(matriz[0])):
        retorno.append([])
        for linha in range(len(matriz)):
            retorno[coluna].append(matriz[linha][coluna])

    return retorno

def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print("")
def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat
mat = le(4, 4)
y = funcao(mat)
imprime(y)