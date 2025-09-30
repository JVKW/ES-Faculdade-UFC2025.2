num = int(input("Digite o valor de N: "))

soma = 0
for i in range(1, num+1):
    soma += i

print(f"Soma total de 1 até {num}: {soma}")