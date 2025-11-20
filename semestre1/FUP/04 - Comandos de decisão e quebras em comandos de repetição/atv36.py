def funcao(n):
    fator = 2
    maior = 1

    while fator <= n:
        if n % fator == 0:
            maior = fator
            n = n // fator
        else:
            fator += 1
    
    return maior

x = int(input(""))
y = funcao(x)
print(f"{y}")