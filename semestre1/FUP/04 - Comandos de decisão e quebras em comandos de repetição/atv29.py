def verificar_primo(n):

  if n == 1:
    return 'Nao primo'
    
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return 'Nao primo'
  return 'Primo'

num = int(input())
print(verificar_primo(num))