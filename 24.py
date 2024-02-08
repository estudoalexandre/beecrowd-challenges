import math

def bhaskara(a, b, c):
    n = b**2 - 4*a*c
    
    if n >= 0 and a != 0:
        x1 = (-b + math.sqrt(n)) / (2*a)
        x2 = (-b - math.sqrt(n)) / (2*a)
        return x1, x2
    else:
        return None

A, B, C = map(float, input().split())

raizes = bhaskara(A, B, C)

if raizes:
    print(f"{raizes[0]:.5f}")
    print(f"{raizes[1]:.5f}")
else:
    print("Impossível calcular.")
