# submissão: 09/09/2021

def mult():
    a, b = map(int, input().split())
    if a < b and b % a == 0:
        return print("Sao Multiplos")
    elif b < a and a % b == 0:
        return print("Sao Multiplos")
    else:
        return print("Nao sao Multiplos")

mult()