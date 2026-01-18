nome = input()

arquivo = open(nome, "r")
saida = open(nome + '.out', 'w')

for linha in arquivo:
    nova_linha = ''
    for c in linha:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' \
        or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            nova_linha += '*'
        else:
            nova_linha += c
    saida.write(nova_linha)

arquivo.close()
saida.close()

saida = open(nome + '.out', 'r')
print(saida.read(), end='')
saida.close()