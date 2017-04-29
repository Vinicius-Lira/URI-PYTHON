A, B, C = [float(x) for x in input().split()]

if A < B:
    aux = A
    A = B
    B = aux
    if A < C:
        aux = A
        A = C
        C = aux
    if B < C:
        aux = B
        B = C
        C = aux

if A < C:
    aux = A
    A = C
    C = aux
    if B < C:
        aux = B
        B = C
        C = aux

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
elif A**2 == (B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif (A**2) > ((B**2) + (C**2)):
    print("TRIANGULO OBTUSANGULO")
elif A**2 < ((B**2) + (C**2)):
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO")

if (A == B != C) | (A == C != B) | (B == C != A):
    print("TRIANGULO ISOSCELES")
