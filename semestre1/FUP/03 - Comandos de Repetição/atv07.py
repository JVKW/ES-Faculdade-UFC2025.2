def sum_intervalo(x):
    soma = 0
    for i in range(1, x+1):
        soma += i
    return soma

num = int(input("Digite o valor de N: "))
print(sum_intervalo(num))