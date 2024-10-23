# submissão: 09/09/2021

def menorabc(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    elif z <= x and z <= y:
        return z


def maiorabc(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z

def meioabc(x, y, z):
    if (x >= y and x <= z) or (x >= z and x <= y):
        return x
    elif (y >= x and y <= z) or (y >= z and y <= x):
        return y
    elif (z >= x and z <= y) or (z >= y and z <= x):
        return z

m, n, p = map(float, input().split())

a = maiorabc(m, n, p)
b = meioabc(m, n, p)
c = menorabc(m, n, p)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if (a ** 2) == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")
    if (a ** 2) > (b ** 2) + (c ** 2):
        print("TRIANGULO OBTUSANGULO")
    if (a ** 2) < (b ** 2) + (c ** 2):
        print("TRIANGULO ACUTANGULO")
    if (a == b == c):
        print("TRIANGULO EQUILATERO")
    if (a == b or b == c) and not(a == b and b == c):
        print("TRIANGULO ISOSCELES")