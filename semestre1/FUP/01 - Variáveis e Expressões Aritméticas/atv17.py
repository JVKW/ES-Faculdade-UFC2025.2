premio = float(input("Prêmio: R$"))

aposta1 = float(input("Aposta Jogador A: R$"))
aposta2 = float(input("Aposta Jogador B: R$"))
aposta3 = float(input("Aposta Jogador C: R$"))

total = aposta1 + aposta2 + aposta3

print(f"Jogador 1: R$ {premio * (aposta1/total)}")
print(f"Jogador 2: R$ {premio * (aposta2/total)}")
print(f"Jogador 3: R$ {premio * (aposta3/total)}")