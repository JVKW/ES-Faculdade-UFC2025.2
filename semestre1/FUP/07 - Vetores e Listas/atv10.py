vetor = []

for i in range(20):
    val = int(input())
    if val >= 0:
        vetor.append(val)
        continue
    vetor.append(0)

for i in vetor:
    print(i)