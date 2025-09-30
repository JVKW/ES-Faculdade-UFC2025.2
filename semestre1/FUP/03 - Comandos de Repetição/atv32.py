txt = input("Digite um texto: ")
novo_txt = ''

for letra in txt:
    novo_txt += chr(ord(letra) + 1)

print(f"Novo texto: {novo_txt}")