def cal_fat_num(x):
    prod = 1
    for i in range(x):
        prod *= i + 1

    soma = 0
    while prod > 0:
        soma += prod % 10
        prod //= 10
    return soma

num = int(input("Digite um número: "))
print(f"A soma dos dígitos de {num}! => {cal_fat_num(num)}")