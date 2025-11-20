def funcao(string, desloc):
    alfabeto_M = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto_codificado = ''
    
    for letra in string:
        encontrado = False
        for pos in range(len(alfabeto_m)):
            if letra == alfabeto_m[pos]:
                encontrado = True
                nova_pos = (pos + desloc) % 26
                texto_codificado += alfabeto_m[nova_pos]
                break

        if encontrado == False:
            for pos in range(len(alfabeto_M)):
                if letra == alfabeto_M[pos]:
                    encontrado = True
                    nova_pos = (pos + desloc) % 26
                    texto_codificado += alfabeto_M[nova_pos]
                    break
    
        if encontrado == False:
            texto_codificado += letra

    return texto_codificado

string = input()
print(funcao(string))