vetor = []

for i in range(0, 10):
  val = float(input())
  vetor.append(val)

for i in range(0, len(vetor)):
  vetor.append(vetor[i]**2)

for i in vetor:
  print(f"{i:.2f}")
