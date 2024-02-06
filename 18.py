tempo_gasto = int(input())
velocidade = int(input())


distancia = tempo_gasto * velocidade
litros_km = 12
consumo = distancia / litros_km


print(f"{consumo:.3f}")