def soma_val(a, b, c):
    soma_quadrado = a ** 2 + b ** 2 + c ** 2
    quadrado_soma = (a + b + c)**2

    return soma_quadrado, quadrado_soma

soma_quadrado, quadrado_soma = soma_val(10, 5, 2)

print(f"Soma do Quadrado = {soma_quadrado}")
print(f"Quadrado da Soma = {quadrado_soma}")