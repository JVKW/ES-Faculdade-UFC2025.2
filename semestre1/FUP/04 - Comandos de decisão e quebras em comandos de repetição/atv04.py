maior = 0
i = 0

while i < 3:
    num = float(input(f"Digite o número {i + 1}: "))
    if i == 0:
        maior = num
    elif num > maior:
        maior = num
    i += 1

print("O maior número é:", maior)