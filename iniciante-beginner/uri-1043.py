# submissão: 09/09/2021

x, y, z = map(float, input().split())

def triangulo(a, b, c):
    if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c ) and (abs(a - b) < c < a + b):
        perimetro = a + b + c
        return print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((a + b) * c )/2
        return print(f"Area = {area:.1f}")

triangulo(x, y, z)