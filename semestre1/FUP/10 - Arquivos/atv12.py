nome = input()
arquivo = open(nome, 'r')

num_caracteres = 0
num_linhas = 0
num_palavras = 0

letras = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

cont = []
for _ in range(26):
    cont.append(0)

dentro_palavra = False
for linha in arquivo:
    num_linhas += 1

    for c in linha:
        num_caracteres += 1

        if c == ' ' or c == '\n' or c == '\t':
            dentro_palavra = False
        else:
            if dentro_palavra == False:
                num_palavras += 1
                dentro_palavra = True

        for i in range(26):
            if c == letras[i] or c == chr(ord(letras[i]) - 32):
                cont[i] += 1

arquivo.close()

print(num_caracteres)
print(num_linhas)
print(num_palavras)

for i in range(26):
    print(letras[i] + ': ' + str(cont[i]))
