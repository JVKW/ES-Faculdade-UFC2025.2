nome_entrada = input()
dia_hoje = int(input())
mes_hoje = int(input())
ano_hoje = int(input())

arquivo = open(nome_entrada, 'r')

nome_saida = nome_entrada + '.out'
arquivo_saida = open(nome_saida, 'w')

for linha in arquivo:
    partes = linha.split('\t')

    nome = partes[0]
    data = partes[1].split(' ')

    dia_nasc = int(data[0])
    mes_nasc = int(data[1])
    ano_nasc = int(data[2])

    idade = ano_hoje - ano_nasc

    if mes_hoje < mes_nasc:
        idade -= 1
    else:
        if mes_hoje == mes_nasc:
            if dia_hoje < dia_nasc:
                idade -= 1

    arquivo_saida.write(nome + '\t' + str(idade) + '\n')

arquivo.close()
arquivo_saida.close()

arquivo_saida = open(nome_saida, 'r')
for linha in arquivo_saida:
    print(linha, end='')
arquivo_saida.close()