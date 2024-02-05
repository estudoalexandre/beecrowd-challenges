peso_a = 2
peso_b = 3
peso_c = 5

a = float(input("Digite: "))
b = float(input("Digite: "))
c = float(input("Digite: "))

sum_media = (a * peso_a) + (b * peso_b) + (c *peso_c)
nota_final = sum_media / (peso_a + peso_b + peso_c)

print(f"MEDIA = {nota_final:.1f}")