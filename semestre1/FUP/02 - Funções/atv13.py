def dividir_premio(valor_total):
    ganhador1 = valor_total * 0.46
    ganhador2 = valor_total * 0.32
    ganhador3 = valor_total - (ganhador1 + ganhador2)

    return ganhador1, ganhador2, ganhador3

ganhador1, ganhador2, ganhador3 = dividir_premio(1000000)

print(f"Ganhador 1: R$ {ganhador1}")
print(f"Ganhador 2: R$ {ganhador2}")
print(f"Ganhador 3: R$ {ganhador3}")