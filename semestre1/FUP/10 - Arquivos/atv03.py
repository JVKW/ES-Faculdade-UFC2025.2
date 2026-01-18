nome = input()

arquivo = open(nome, "r")

contador = 0
for linha in arquivo:
    for letra in linha:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' \
        or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            contador = contador + 1

arquivo.close()

print(contador)