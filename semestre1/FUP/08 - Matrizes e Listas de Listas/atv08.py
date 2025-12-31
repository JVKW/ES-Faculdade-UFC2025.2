def funcao(matriz):
    soma = 0
    for linha in range(len(matriz)):
        for coluna in range(linha + 1, len(matriz[linha])):
            soma += matriz[linha][coluna]

    return soma

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
print(y)