
def funcao(data):
    meses = [
        "janeiro",
        "fevereiro",
        "marco",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro"
    ]

    if data[0:2][0] == '0':
      dia = int(data[1])
    else:
      dia = int(data[0:2])
    if data[3:5][0] == '0':
      mes = int(data[4])
    else:
      mes = int(data[3:5])
    ano = int(data[6::])

    return f'{dia} de {meses[mes-1]} de {ano}'

data = '10/05/2003'

# x = input("")
y = funcao(data)
print(f"{y}")