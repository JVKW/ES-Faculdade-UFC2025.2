def repartir_premio(premio, ap1, ap2, ap3):
    total = ap1 + ap2 + ap3
    ganhador1 = premio * (ap1 / total)
    ganhador2 = premio * (ap2 / total)
    ganhador3 = premio * (ap3 / total)
    return ganhador1, ganhador2, ganhador3

g1, g2, g3 = repartir_premio(1000000, 500, 300, 100)

print(f"O Jogadores Ganharam, respectivamente: R${g1:.2f}, R${g2:.2f}, R${g3:.2f}")
