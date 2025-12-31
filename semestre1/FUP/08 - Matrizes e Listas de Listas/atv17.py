def eh_primo(n):
    nabs = abs(n)
    
    if nabs == 0: 
        return False
    
    if nabs == 1 or nabs ==  2:
        return True

    for d in range(2, nabs):
        if nabs % d == 0:
            return False
    return True


def funcao(matriz):
    vetor = []

    for linha in range(len(matriz)):
        vetor.append([])

    for coluna in range(len(matriz[0])):
        menor = matriz[0][coluna]
        tem_primo = False
        maior_primo = 0

        for linha in range(len(matriz)):
            num = matriz[linha][coluna]

            if num < menor:
                menor = num

            if eh_primo(num):
                if not tem_primo:
                    maior_primo = num
                    tem_primo = True
                elif num > maior_primo:
                    maior_primo = num

        for linha in range(len(matriz)):
            if tem_primo:
                vetor[linha].append(matriz[linha][coluna] / maior_primo)
            else:
                vetor[linha].append(matriz[linha][coluna] / menor)

    return vetor


def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]:.2f} ", end="")
        print("")
def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat
mat = le(12, 13)
y = funcao(mat)
imprime(y)