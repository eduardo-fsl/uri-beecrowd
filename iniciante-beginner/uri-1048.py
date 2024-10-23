#20/03/2023

salario = float(input())

if 0 <= salario <= 400:
    novo_salario = salario * 1.15
    percentual = 15

elif 400 < salario <= 800:
    novo_salario = salario * 1.12
    percentual = 12

elif 800 < salario <= 1200:
    novo_salario = salario * 1.10
    percentual = 10

elif 1200 < salario <= 2000:
    novo_salario = salario * 1.07
    percentual = 7
else:
    novo_salario = salario * 1.04
    percentual = 4

print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {novo_salario - salario:.2f}\nEm percentual: {percentual} %")