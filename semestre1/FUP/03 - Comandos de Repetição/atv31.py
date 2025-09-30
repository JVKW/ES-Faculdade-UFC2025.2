f1 = input("Digite a frase 1: ")
f2 = input("Digite a frase 2: ")
n = int(input("Digite N: "))
str = f'{f1}'

x = 1
while x <= n:
    str += f' {f2}'
    x += 1

print(str)