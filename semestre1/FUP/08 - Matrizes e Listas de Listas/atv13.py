def funcao(matriz):
    vetor = []

    for coluna in range(len(matriz[0])):
        soma = 0
        for linha in range(len(matriz)):
            soma += matriz[linha][coluna]

        vetor.append(soma)
    
    return vetor


def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat
mat = le(5, 5)
vet = funcao(mat)
print(vet)