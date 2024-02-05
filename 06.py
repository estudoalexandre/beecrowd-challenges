peso_a = 3.5
peso_b = 7.5

nota_a = float(input()) 
nota_b = float(input()) 

sum_media = (nota_a * peso_a) + (nota_b * peso_b)

nota_final = sum_media / (peso_a + peso_b)

print(f"MEDIA = {nota_final:.5f}".replace('.', ','))
