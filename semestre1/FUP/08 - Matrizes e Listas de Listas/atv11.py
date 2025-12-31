def funcao(matriz):
    soma = 0
    cont = 0
    for i in range(len(matriz)-1, -1, -1):
        soma += matriz[cont][i]
        cont += 1

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