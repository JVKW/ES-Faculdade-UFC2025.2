entrada = input()
saida = input()

with open(entrada, 'r') as arq_in:
    conteudo = arq_in.read()

conteudo_maisculo = conteudo.upper()

with open(saida, 'w') as arq_out:
    arq_out.write(conteudo_maisculo)

print(conteudo, end='')
print(conteudo_maisculo, end='')