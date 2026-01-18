nome = input()

arquivo = open(nome, "r")

vogais = 0
consoantes = 0
for linha in arquivo:
    for letra in linha:

        if letra >= 'a' and letra <= 'z':
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1

        elif letra >= 'A' and letra <= 'Z':
            if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1

arquivo.close()

print(vogais)
print(consoantes)