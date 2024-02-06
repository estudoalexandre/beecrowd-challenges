segundos = int(input())

horas, resto = divmod(segundos, 3600)
minutos, segundos = divmod(resto, 60)

tempo = f"{horas}:{minutos}:{segundos}"

print(tempo)