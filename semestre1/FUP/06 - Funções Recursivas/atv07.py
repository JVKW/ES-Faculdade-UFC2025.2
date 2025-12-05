def funcao(n):
    if n > 0:
        funcao(n - 1)
    if n % 2 == 0:
        print(n)
