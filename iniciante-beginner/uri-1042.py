# submissão: 10/09/2021

a, b, c = map(int, input().split())

def menorabc(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < x and z < y:
        return z


def maiorabc(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z

def meioabc(x, y, z):
    if (x > y and x < z) or (x > z and x < y):
        return x
    elif (y > x and y < z) or (y > z and y < x):
        return y
    elif (z > x and z < y) or (z > y and z < x):
        return z


print(menorabc(a, b, c))
print(meioabc(a, b, c))
print(maiorabc(a, b, c))
print('')
print(a)
print(b)
print(c)