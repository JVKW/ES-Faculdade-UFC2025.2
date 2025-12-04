A = int(input())
B = int(input())
C = int(input())

if not (A < B + C and B < A + C and C < A + B):
    print("Nao triangulo")
else:
    if A == B and B == C:
        print("Triangulo equilatero")
    elif A == B or A == C or B == C:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
