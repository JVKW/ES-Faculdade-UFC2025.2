rep = int(input())

cont_maior = 1
maior = int(input())

for i in range(2, rep + 1):
    num = int(input())
        
    if num > maior:
        maior = num
        cont_maior = 1
    else:
        if num == maior:
            cont_maior += 1
    
print(maior)
print(cont_maior)