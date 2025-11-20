def funcao(txt):
    frase = ""
    i = 0
    while i < len(txt):
        c = txt[i]
        codigo = ord(c)
        if codigo >= 65:
            if codigo <= 90:
                frase += chr(codigo + 32)
        if codigo >= 97:
            if codigo <= 122:
                frase += c
        i = i + 1

    inverso = ""
    j = len(frase) - 1
    while j >= 0:
        inverso += frase[j]
        j = j - 1

    if frase == inverso:
        print(True)
    else:
        print(False)

funcao(input())
