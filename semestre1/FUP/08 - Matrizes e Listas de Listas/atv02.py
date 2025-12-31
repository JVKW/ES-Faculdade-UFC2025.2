def function(n):
    matriz = []
    for linha in range(n):
        matriz.append([])
        for coluna in range(n):
            if linha == coluna:
                matriz[linha].append(1)
            else:
                matriz[linha].append(0)
    
    return matriz

x = int(input(""))
m = function(x)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(f"{m[i][j]} ", end="")
    print("")