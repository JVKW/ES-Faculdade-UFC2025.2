nome = input()

arquivo = open(nome, 'r')

linhas = 0
for i in arquivo:
    linhas += 1

arquivo.close()

print(linhas)