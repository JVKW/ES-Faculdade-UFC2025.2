nome = input()

arquivo = open(nome, 'r')

letras = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

cont = []
for _ in range(26):
    cont.append(0)

for linha in arquivo:
    for c in linha:
        for i in range(26):
            if c == letras[i] or c == chr(ord(letras[i]) - 32):
                cont[i] += 1

arquivo.close()

for i in range(26):
    print(f'{letras[i]}: {cont[i]}')