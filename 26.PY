tabela = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

codigo, quantidade = map(int, input().split())


if codigo in tabela:
    valor_total = tabela[codigo] * quantidade
    print(f"Total: R$: {valor_total:.2f}")
else:
    print("Codigo do item invalido")
    





