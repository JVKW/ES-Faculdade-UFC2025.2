def triangulo_floyd(n):
    soma = 1
    for l in range(1, n+1):
        for _ in range(1, l + 1):
            print(soma, end=" ")
            soma += 1
        print()

num = int(input("Digite o valor de N: "))

triangulo_floyd(num)