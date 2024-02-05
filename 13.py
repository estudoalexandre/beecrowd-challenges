lado_a, lado_b, raio = map(float, input().split())

pi = 3.14159
triangulo = 0.5 * ( lado_a * raio)
circulo = pi * (raio ** 2)
trapezio = ((lado_a + lado_b) * raio) / 2
quadrado = lado_b ** 2
retangulo = lado_a * lado_b


print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")