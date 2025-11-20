soma = 0
for i in range(4):
    num = int(input(f"Digite o número {i + 1}: "))
    if num % 2 == 0:
        soma += num
    
print("Soma Total dos Pares:", soma)