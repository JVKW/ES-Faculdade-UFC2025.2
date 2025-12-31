def funcao(A, B):
    matriz = []

    for linha in range(len(A)):
        matriz.append([])
        for coluna in range(len(A[linha])):
            rA = A[linha][coluna]
            rB = B[linha][coluna]
            if rA > rB:
                matriz[linha].append(rA)
            else:
                matriz[linha].append(rB)

    return matriz


def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat
def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print("")
mat1 = le(4, 4)
mat2 = le(4, 4)
y = funcao(mat1, mat2)
imprime(y)