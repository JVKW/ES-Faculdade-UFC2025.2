idade = int(input())
tempo_servico = int(input())

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Pode se aposentar")
else:
    print("Nao pode se aposentar")