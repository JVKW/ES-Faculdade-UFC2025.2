saque = float(input("Valor do Saque: "))
res = 0

nota100 = int(saque // 100)
res = saque % 100

nota50 = int(res // 50)
res = res % 50

nota20 = int(res // 20)
res = res % 20

nota10 = int(res // 10)
res = res % 10

nota5 = int(res // 5)
res = res % 5

nota2 = int(res // 2)
res = res % 2

nota1 = int(res // 1)
res = res % 1


print(f"Notas de 100: ", nota100)
print(f"Notas de 50: ", nota50)
print(f"Notas de 20: ", nota20)
print(f"Notas de 10: ", nota10)
print(f"Notas de 5 : ", nota5)
print(f"Notas de 2: ", nota2)
print(f"Moedas de 1 Real: ", nota1)
print("Resto: R$", res)
