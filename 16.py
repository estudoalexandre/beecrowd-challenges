import math

x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())

distancia = ((x2 - y2)**2) + ((x1 - y1)** 2)

resultado = distancia ** 0.5

print(f"{resultado:.4f}")