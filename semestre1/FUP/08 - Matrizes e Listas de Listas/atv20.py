def verificar_produto(vetor, seq=4):
    maior = 0
    indice_i = 0

    for i in range(len(vetor) - (seq - 1)):
        produto = 1
        for j in range(seq):
            produto *= vetor[i + j]

        if produto > maior:
            maior = produto
            indice_i = i
    
    return maior, indice_i

def funcao(matriz, seq):
    linhas = len(matriz)
    colunas = len(matriz[0])

    maior = 0
    melhor_linha = 0
    melhor_coluna = 0
    direcao = ''

    # horizontal
    for linha in range(linhas):
        vetor_produto, col = verificar_produto(matriz[linha], seq)
        if vetor_produto > maior:
            maior = vetor_produto
            melhor_linha = linha
            melhor_coluna = col
            direcao = 'direita'
            
    # vertical
    for coluna in range(colunas):
        vetor_c = []
        for linha in range(linhas):
            vetor_c.append(matriz[linha][coluna])
        
        vetor_produto, lin = verificar_produto(vetor_c, seq)
        if vetor_produto > maior:
            maior = vetor_produto
            melhor_linha = lin
            melhor_coluna = coluna
            direcao = 'baixo'

    # diagonal
    for linha in range(linhas):
        for coluna in range(colunas):

            # principal
            if (linha + seq - 1 < linhas) and (coluna + seq - 1 < colunas):
                vetor_d = []

                for k in range(seq):
                    vetor_d.append(matriz[linha + k][coluna + k])

                vetor_produto, _ = verificar_produto(vetor_d, seq)
                if vetor_produto > maior:
                    maior = vetor_produto
                    melhor_linha = linha
                    melhor_coluna = coluna
                    direcao = 'direita baixo'

            # secundária
            if (linha + seq - 1 < linhas) and (coluna - (seq - 1) >= 0):
                vetor_d = []

                for k in range(seq):
                    vetor_d.append(matriz[linha + k][coluna - k])

                vetor_produto, _ = verificar_produto(vetor_d, seq)
                if vetor_produto > maior:
                    maior = vetor_produto
                    melhor_linha = linha
                    melhor_coluna = coluna
                    direcao = 'esquerda baixo'

    return maior, melhor_linha, melhor_coluna, direcao

def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat
mat = le(20, 20)
x = 4
y1,y2,y3,y4 = funcao(mat, x)
print(y1)
print(y2)
print(y3)
print(y4)