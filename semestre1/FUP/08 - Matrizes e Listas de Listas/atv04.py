def funcao(matriz):
    maior = matriz[0][0]
    cord = []
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            val = matriz[linha][coluna]
            if val > maior:
                maior = val
                cord = [linha, coluna] 
    
    return maior, cord[0], cord[1]

mat = []
for i in range(4):
    mat.append([])
    for j in range(4):
        num = int(input(""))
        mat[i].append(num)
y1,y2,y3 = funcao(mat)
print(y1)
print(y2)
print(y3)