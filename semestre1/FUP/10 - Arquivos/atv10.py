arq_in_name = input()
arq_out_name = input()

arquivo = open(arq_in_name, 'r')

lista = []
for linha in arquivo:
    partes = linha.split('\t')
    nome = partes[0]
    habitantes = int(partes[1])

    lista.append({
        'nome': nome,
        'habitantes': habitantes
    })

arquivo.close()

for item in lista:
    print(item)

maior_nome = lista[0]['nome']
maior_hab = lista[0]['habitantes']

for i in range(1, len(lista)):
    if lista[i]['habitantes'] > maior_hab:
        maior_nome = lista[i]['nome']
        maior_hab = lista[i]['habitantes']

arquivo_saida = open(arq_out_name, 'w')
arquivo_saida.write(maior_nome + '\t' + str(maior_hab))
arquivo_saida.close()

arquivo_saida = open(arq_out_name, 'r')
for linha in arquivo_saida:
    print(linha, end='')
arquivo_saida.close()