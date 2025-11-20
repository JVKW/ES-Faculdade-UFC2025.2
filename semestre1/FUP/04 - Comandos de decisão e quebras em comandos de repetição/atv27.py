def verificar_numero(n):
  maior = 0
  menor = 0

  for i in range(1, n+1):
    num = float(input())

    if i == 1:
      maior = num
      menor = num

    if num > maior:
      maior = num
    if num < menor:
      menor = num
  return maior, menor
  
quantidade = int(input())

maior, menor = verificar_numero(quantidade)

print(f"{menor:.2f}")
print(f"{maior:.2f}")