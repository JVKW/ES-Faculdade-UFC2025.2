def contar_brancos(p):
    soma = 0
    for i in str(p):
        if i == ' ':
            soma += 1
    
    return soma

p1 = str(input())
print(contar_brancos(p1))