arquivo = open('arq.txt', 'w')

while True:
    linha = input()
    if linha == '0':
        break
    arquivo.write(linha + '\n')

arquivo.close()

arquivo = open('arq.txt', 'r')

print(arquivo.read(), end='')
arquivo.close()