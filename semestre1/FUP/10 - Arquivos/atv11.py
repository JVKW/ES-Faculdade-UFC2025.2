def funcao(nome_arquivo, palavra):
    arquivo = open(nome_arquivo, 'r')

    cont = 0
    palavra = palavra.lower()
    tam = len(palavra)
    for linha in arquivo:
        linha = linha.lower()
        i = 0
        while i <= len(linha) - tam:
            if linha[i:i+tam] == palavra:
                cont += 1
            i += 1

    arquivo.close()
    return cont

x1 = input()
x2 = input()
y = funcao(x1, x2)
print(f"{y}")