valor_a, valor_b, valor_c = map(float, input().split())

abs_1 = abs(valor_a - valor_b)

maior_ab = valor_a + valor_b + abs_1

maior_ab = maior_ab / 2

abs_2 = abs(maior_ab - valor_c)

maior_ab = maior_ab + valor_c + abs_2

maior_ab = maior_ab / 2

print(f"{int(maior_ab)} eh o maior")