soma = 0
denominador = 1

for i in range(1, 100, 2):
    soma += i / denominador
    denominador += 1

print(f"S = {soma:.6f}")