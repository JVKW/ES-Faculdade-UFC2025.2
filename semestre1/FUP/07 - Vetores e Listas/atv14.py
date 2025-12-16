import random

seed_x = int(input())

random.seed(seed_x)
vetor = []
for i in range(12):
    vetor.append(random.uniform(-10, 10))

soma = 0
negativos = 0
for i in vetor:
    if i > 0:
        soma += i
    else:
        negativos += 1
    
print(negativos)
print(f"{soma:.2f}")