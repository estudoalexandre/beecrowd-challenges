money = float(input()) * 100 
print(money)

notas = [10000, 5000, 2000, 1000, 500, 200] 
moedas = [100, 50, 25, 10, 5, 1] 
print("NOTAS:")
for nota in notas:
    qtd_notas = money // nota
    money %= nota
    print(f"{int(qtd_notas)} nota(s) de R$ {nota/100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = money // moeda
    money %= moeda
    print(f"{int(qtd_moedas)} moeda(s) de R$ {moeda/100:.2f}")

