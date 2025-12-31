def funcao(A, B):
    produto = []

    for linha in range(len(A)):
        produto.append([])
        for coluna in range(len(B[0])):
            soma = 0
            for cont in range(len(A[0])):
                soma += A[linha][cont] * B[cont][coluna]
            
            produto[linha].append(soma)

    return produto

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
mat1 = le(5, 5)
mat2 = le(5, 5)
y = funcao(mat1, mat2)
imprime(y)