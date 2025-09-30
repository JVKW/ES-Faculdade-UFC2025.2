def som_imp(x):
    sum = 0
    for i in range(0, x):
        sum += 2 * i
    return sum

num = int(input("Digite um número: "))

print(f"Os {num} primeiros números pares são: {som_imp(num)}")