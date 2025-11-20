def contar_1(p):
    soma = 0
    for i in str(p):
        if i == '1':
            soma += 1
    
    return soma

p1 = str(input())
print(contar_1(p1))