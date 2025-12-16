string = input("")

retorno = []

for c in string:
    if c == " " or c == "-":
        continue
    
    achou = False

    for r in retorno:
        if r == c:
            achou = True
            break
    
    if not achou:
        retorno.append(c)

print(len(retorno))