def funcao(A, B):
    somaAB = []

    for linha in range(len(A)):
        somaAB.append([])
        for coluna in range(len(A[0])):
            somaAB[linha].append(A[linha][coluna] + B[linha][coluna])

    return somaAB
            

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
mat1 = le(4, 5)
mat2 = le(4, 5)
y = funcao(mat1, mat2)
imprime(y)