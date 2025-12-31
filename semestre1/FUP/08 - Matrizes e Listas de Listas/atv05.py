def funcao(matriz, num):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == num:
                return linha, coluna

    return -1, -1

mat = []
for i in range(5):
    mat.append([])
    for j in range(5):
        num = int(input(""))
        mat[i].append(num)
x = int(input(""))
y1,y2 = funcao(mat, x)
print(y1)
print(y2)