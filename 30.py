def verificar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

def calcular_per(a, b, c):
    return a + b + c

def calcular_area_trap(a, b, c):
    return ((a + b) * c) / 2

a, b, c = map(float, input().split())

if verificar_triangulo(a, b, c):
    perimetro = calcular_per(a, b, c)
    print("Perimetro =", perimetro)
else:
    area = calcular_area_trap(a, b, c)
    print("Area =", area)