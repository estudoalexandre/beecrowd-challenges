codigo_produto1, quantidade_produto1, preco_produto1 = map(float, input().split())
codigo_produto2, quantidade_produto2, preco_produto2 = map(float, input().split())


valor_a_pagar = (quantidade_produto1 * preco_produto1) + (quantidade_produto2 * preco_produto2)



print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")
