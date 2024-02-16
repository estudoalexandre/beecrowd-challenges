ddd = [61, 71, 11, 21, 32, 19, 27, 31]
entrada = int(input())


if entrada in ddd and entrada == 61:
    print("Brasilia")
elif entrada in ddd and entrada == 71:
    print("Salvador")
elif entrada in ddd and entrada == 11:
    print("Sao Paulo")
elif entrada in ddd and entrada == 21:
    print("Rio de Janeiro")
elif entrada in ddd and entrada == 32:
    print("Juiz de Fora")
elif entrada in ddd and entrada == 19:
    print("Campinas")
elif entrada in ddd and entrada == 27:
    print("Vitoria")
elif entrada in ddd and entrada == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
    