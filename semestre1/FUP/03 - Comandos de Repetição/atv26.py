def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

def serie_taylor_sen(x, n):
    soma = 0
    for i in range(0, n):
        soma += (-1)**i * (x ** (2 * i + 1))/fatorial(2 * i + 1)
    return soma

rad = float(input("Digite o valor de N: "))

print(serie_taylor_sen(rad, 10))