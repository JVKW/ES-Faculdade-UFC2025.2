nome = input()
str_out = ''

for i in nome:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        continue
    str_out = str_out + i

print(str_out)
