# lista = [3, 1, 4, 1, 5, 9, 2, 6]
# ordenada_crescente = sorted(lista)

# print(ordenada_crescente)

# ordenada_decrescente = sorted(lista, reverse=True)
# print("Ordem decrescente:", ordenada_decrescente)


def ordenar(x, y, z):
    lista = [x, y, z]
    lista_cresc = sorted(lista)
    for lista_x in lista_cresc:
        print(f"{lista_x}")
    print()
    for lista_y in lista:
        print(lista_y)
    
x, y, z = map(int, input().split())

ordenar(x, y, z)