#submissão: 10/08/2021

codigo_peca1, numero_peca1, valor_unitario_peca1 = map(float, input().split())
codigo_peca2, numero_peca2, valor_unitario_peca2 = map(float, input().split())

codigo_peca1 = int(codigo_peca1)
numero_peca1 = int(numero_peca1)
codigo_peca2 = int(codigo_peca2)
numero_peca2 = int(numero_peca2)

valor_total = numero_peca1 * valor_unitario_peca1 + numero_peca2 * valor_unitario_peca2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")