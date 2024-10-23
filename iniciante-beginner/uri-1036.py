# submissão: 26/08/2021

import math

x, y, z = map(float, input().split())


# preciso calcular o delta e usá-lo na formula de equação quadrática.

# delta = (b ** 2) - (4 * a * c)

def raizes(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0 or a == 0:
        print("Impossivel calcular")
        return raizes
    if delta == 0:
        raiz1 = (-b - (math.sqrt(delta))) / (2 * a)
        print(f"R1 = {raiz3:.5f}")
        print(f"R1 = {raiz3:.5f}")
    if delta > 0:
        raiz2 = (-b - (math.sqrt(delta))) / (2 * a)
        raiz3 = (-b + (math.sqrt(delta))) / (2 * a)
        if raiz2 > raiz3:
            print(f"R1 = {raiz2:.5f}")
            print(f"R2 = {raiz3:.5f}")
        if raiz3 > raiz2:
            print(f"R1 = {raiz3:.5f}")
            print(f"R2 = {raiz2:.5f}")


raizes(x, y, z)
