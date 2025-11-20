num1 = float(input("Digite o valor 1: "))
num2 = float(input("Digite o valor 2: "))
num3 = float(input("Digite o valor 3: "))

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

if num1 > num3:
    aux = num1
    num1 = num3
    num3 = aux

if num2 > num3:
    aux = num2
    num2 = num3
    num3 = aux

print(f"Ordem Crescente: {num1} , {num2} , {num3}")