hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())


inicio_minutos = hora_inicio * 60 + minuto_inicio
final_minutos =  hora_fim * 60 + minuto_fim

duracao_total = final_minutos - inicio_minutos



if duracao_total < 1:
    duracao_total += 24 * 60
elif duracao_total > 24 * 60:
    duracao_total %= 24 * 60
    

hora_final = duracao_total // 60
minuto_final = duracao_total % 60

print(f"O JOGO DUROU {hora_final} HORA(S) E {minuto_final} MINUTO(S)")