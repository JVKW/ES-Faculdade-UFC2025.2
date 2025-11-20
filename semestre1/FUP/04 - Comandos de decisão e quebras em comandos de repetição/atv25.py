soma = 0
contador = 0

while contador < 10:
    num = int(input())
    if num > 0:
        soma += num
        contador += 1

print(f'{soma/10:.2f}')
