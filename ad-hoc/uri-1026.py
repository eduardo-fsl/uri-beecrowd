# submissão: 01/02/2024

def operador(a, b):
    return print(a ^ b)

while True:
    try:
        m, n = map(int, input().split())
        operador(a=m, b=n)
    except EOFError:
        break
