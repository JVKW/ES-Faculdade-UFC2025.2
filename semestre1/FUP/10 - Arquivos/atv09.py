arq1 = input()
arq2 = input()

f1 = open(arq1, 'r')
f2 = open(arq2, 'r')

nome_saida = arq1 + arq2
f3 = open(nome_saida, 'w')

for linha in f1:
    f3.write(linha)

for linha in f2:
    f3.write(linha)

f1.close()
f2.close()
f3.close()

f3 = open(nome_saida, 'r')
for linha in f3:
    print(linha, end='')
f3.close()