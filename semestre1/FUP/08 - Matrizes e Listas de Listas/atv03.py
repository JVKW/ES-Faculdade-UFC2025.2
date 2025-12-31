def funcao(n):
    matriz = []
    for linha in range(n):
        matriz.append([])
        for coluna in range(n):
            matriz[linha].append(linha * coluna)
    
    return matriz

x = int(input(""))
m = funcao(x)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(f"{m[i][j]} ", end="")
    print("")