def verificar_palavras(palavra1, palavra2):
    if len(palavra1) < len(palavra2):
        menor = len(palavra1)
    else:
        menor = len(palavra2)

    for i in range(menor):
        if palavra1[i] < palavra2[i]:
            return palavra1
        elif palavra1[i] > palavra2[i]:
            return palavra2
        
    if len(palavra1) < len(palavra2):
        return palavra1
    else:
        return palavra2
    
p1 = str(input())
p2 = str(input())

print(verificar_palavras(p1, p2))