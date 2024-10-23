# submissão: 14/02/2023

valor = float(input())

cedulas = [100, 50, 20, 10, 5, 2]

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print(f"NOTAS:")
for notas in cedulas:
    i = valor // notas
    print(f"{int(i)} nota(s) de R$ {notas:.2f}")
    valor -= i * notas

print(f"MOEDAS:")
for moeda in moedas:
    j = int(round(valor,2) / moeda)
    print(f"{int(j)} moeda(s) de R$ {moeda:.2f}")
    valor -= j * moeda