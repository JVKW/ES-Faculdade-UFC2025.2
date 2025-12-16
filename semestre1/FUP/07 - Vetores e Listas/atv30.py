def funcao(lista):


    for tam in range(len(lista) - 1, 1, -1): # 5 => 2
        for i in range(len(lista) - tam): # 0 => 5
            for j in range(i + 1, len(lista) - tam + 1): # 1 => 5

                iguais = True
                for k in range(tam): # 0 => 5
                    if lista[i + k] != lista[j + k]:
                        iguais = False
                        break
                
                if iguais:
                    return i, j, tam
            
    return -1, -1, -1

x = []
for i in range(10):
    x.append(int(input("")))
y1, y2, y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")