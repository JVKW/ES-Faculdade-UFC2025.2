notas = []

soma = 0
for i in range(15):
    val = float(input())
    notas.append(val)
    soma += val

print(f"{(soma/len(notas)):.2f}")