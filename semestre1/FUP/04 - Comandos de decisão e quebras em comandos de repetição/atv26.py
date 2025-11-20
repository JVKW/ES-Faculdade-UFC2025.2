contador = 0

while contador < 10:
    num = float(input())
    if contador == 0:
        maior = num
        menor = num
    
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    contador += 1

print(f"{menor:.2f}")
print(f"{maior:.2f}")