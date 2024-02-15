hora_inicial, hora_final = map(int, input().split())

duracao = hora_final - hora_inicial



if hora_final < hora_inicial:
    duracao += 24
    
if duracao < 1:
    duracao += 24
elif duracao > 24:
    duracao -= 24
    

print(f"O JOGO DUROU {duracao} HORA(S)")