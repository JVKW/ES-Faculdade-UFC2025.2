vetor = []
for i in range(100):
    val = float(input())
    vetor.append(val)

while True:
    cod = int(input())
    if cod == 1:
        for i in vetor:
            print(f"{i:.1f}")
    elif cod == 2:
        for i in range(len(vetor)-1, -1, -1):
            print(f"{vetor[i]:.1f}")
    elif cod != 0:
        print("Codigo invalido")
    elif cod == 0:
        break