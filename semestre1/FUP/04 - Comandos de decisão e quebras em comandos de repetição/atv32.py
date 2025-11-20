n1 = int(input())
n2 = int(input())

if n1 >= n2:
    dividendo = n1
    divisor = n2
else:
    dividendo = n2
    divisor = n1

resto = dividendo
resultado = 0

while resto >= divisor:
    resto -= divisor
    resultado += 1

print(resultado)