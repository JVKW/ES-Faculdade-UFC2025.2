nome = input()
caractere = input()

arquivo = open(nome, "r")

contador = 0
for linha in arquivo:
    for c in linha:
        if c == caractere:
            contador += 1

arquivo.close()

print(contador)