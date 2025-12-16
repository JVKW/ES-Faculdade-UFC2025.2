valores = []

for i in range(1, 11):
    num = int(input())

    valores.append(num)

for i in range(len(valores)-1, -1, -1):
  print(valores[i])