x = input("Digite uma frase: ")
str = ''

for i in x[::-1]:
    str += i

print(str)