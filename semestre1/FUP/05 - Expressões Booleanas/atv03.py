palavra = input()
caractere = input()

if len(caractere) > 0:
    rep = caractere[0]
else:
    rep = ''

vogais = "aeiouAEIOU"

qtd = 0
nova = ""

i = 0
while i < len(palavra):
    c = palavra[i]

    eh_vogal = 0
    j = 0
    while j < len(vogais):
        if c == vogais[j]:
            eh_vogal = 1
            qtd = qtd + 1
            break
        j = j + 1

    if eh_vogal == 1:
        nova = nova + rep
    else:
        nova = nova + c

    i = i + 1

print(qtd)
print(nova)
