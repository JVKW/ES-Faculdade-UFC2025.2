num = int(input("Número de 1000 a 9999: "))

print(num // 1000)
print((num // 100) % 10)
print((num // 10) % 10)
print(num % 10)