# submissão: 10/08/2021

nome = input()
salario_fixo = float(input())
total_de_vendas = float(input())

salario_total = salario_fixo + total_de_vendas*0.15

print(f"TOTAL = R$ {salario_total:.2f}")