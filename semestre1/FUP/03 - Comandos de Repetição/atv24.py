def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

def triangulo_pascal(x):
    for n in range(x):
        for k in range(0, n+1):
            valor = fatorial(n) // (fatorial(k) * fatorial(n - k))
            print(valor, end=" ")
        print()


num = int(input("Digite o valor de N: "))

triangulo_pascal(num)