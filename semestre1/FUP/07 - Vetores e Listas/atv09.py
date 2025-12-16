vetor = []

for i in range(10):
    val = int(input())
    vetor.append(val)

maior = vetor[0]
menor = vetor[0]

for num in vetor:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(maior)
print(menor)
