# submissão: 26/08/2021

a = float(input())

x = "[0,25]"
y = "(25,50]"
z = "(50,75]"
w = "(75,100]"

if 75 < a <= 100:
    print(f"Intervalo {w}")
if 50 < a <= 75:
    print(f"Intervalo {z}")
if 25 < a <= 50:
    print(f"Intervalo {y}")
if 0 <= a <= 25:
    print(f"Intervalo {x}")
if a < 0 or a > 100:
    print("Fora de intervalo")

