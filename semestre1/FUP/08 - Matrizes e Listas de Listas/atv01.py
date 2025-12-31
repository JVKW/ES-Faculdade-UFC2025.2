def funcao(x):
    cont = 0
    for i in x:
        for y in i:
            if y > 10:
                cont += 1
    
    return cont

mat = []
for i in range(4):
    mat.append([])
    for j in range(4):
        num = int(input(""))
        mat[i].append(num)
y = funcao(mat)
print(f"{y}")