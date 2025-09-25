val_total = float(input("Valor do Prêmio: R$"))

porc_gan1 = 46
porc_gan2 = 32
porc_gan3 = 100 - (porc_gan1 + porc_gan2)

premio1 = val_total * porc_gan1/100
premio2 = val_total * porc_gan2/100
premio3 = val_total * porc_gan3/100

print(f"Ganhador 1: R$ {premio1}")
print(f"Ganhador 2: R$ {premio2}")
print(f"Ganhador 3: R$ {premio3}")