n_notas = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(n_notas)

for n in notas:
    quantidade = n_notas // n
    
    n_notas %= n
    print(f"{quantidade} nota(s) de R$ {n},00")


 