n1 = int(input())

soma = 0
for i in range(1, n1):
    if n1 % i == 0:
        soma += i

if soma == n1:
    print("Perfeito")
else:
    print("Nao Perfeito")