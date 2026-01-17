from math import sin, cos

def converterPolarRadiano(vetor):
    return {
        'x': vetor['r'] * cos(vetor['a']),
        'y': vetor['r'] * sin(vetor['a'])
    }

raio = float(input())
angulo = float(input())

coordPolar = {'r': raio, 'a': angulo}

print(coordPolar)
print(converterPolarRadiano(coordPolar))