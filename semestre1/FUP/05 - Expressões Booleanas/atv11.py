def funcao(data):
    if (len(data) != 10) or (data [2] != '/' or data[5] != '/'):
        return 0, 0, 0

    if ord(data[0]) < 48 or ord(data[0]) > 57: return 0, 0, 0
    if ord(data[1]) < 48 or ord(data[1]) > 57: return 0, 0, 0
    if ord(data[3]) < 48 or ord(data[3]) > 57: return 0, 0, 0
    if ord(data[4]) < 48 or ord(data[4]) > 57: return 0, 0, 0
    if ord(data[6]) < 48 or ord(data[6]) > 57: return 0, 0, 0
    if ord(data[7]) < 48 or ord(data[7]) > 57: return 0, 0, 0
    if ord(data[8]) < 48 or ord(data[8]) > 57: return 0, 0, 0
    if ord(data[9]) < 48 or ord(data[9]) > 57: return 0, 0, 0

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    return dia, mes, ano
