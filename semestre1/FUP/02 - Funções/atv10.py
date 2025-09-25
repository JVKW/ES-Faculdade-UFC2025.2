from math import pi

def conv_graus(graus):
    return (graus * pi)/180

resp = conv_graus(180)

print(f"{resp:.2f}rad")