def contar_dinheiro(saque):
    resto = saque

    nota100 = resto // 100
    resto = resto % 100

    nota50 = resto // 50
    resto = resto % 50

    nota20 = resto // 20
    resto = resto % 20

    nota10 = resto // 10
    resto = resto % 10

    nota5 = resto // 5
    resto = resto % 5

    nota2 = resto // 2
    resto = resto % 2

    nota1 = resto // 1
    resto = resto % 1

    return nota100, nota50, nota20, nota10, nota5, nota2, nota1

n100, n50, n20, n10, n5, n2, n1 = contar_dinheiro(789)

print(f"Notas de 100: {n100}")
print(f"Notas de 50: {n50}")
print(f"Notas de 20: {n20}")
print(f"Notas de 10: {n10}")
print(f"Notas de 5: {n5}")
print(f"Notas de 2: {n2}")
print(f"Notas de 1: {n1}")