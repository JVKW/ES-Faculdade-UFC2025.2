num = int(input("Número de 100 a 999: "))

cen = num // 100
dez = (num // 10) % 10
uni = num % 10

print(f"Número Invertido: {uni * 100 + dez * 10 + cen}")