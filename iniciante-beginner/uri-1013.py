# submissão 10/08/2021

a, b, c = map(int, input().split())

maior_a_b = (a + b + abs(a - b))/2
maior = (maior_a_b + c + abs(maior_a_b - c))/2
maior = int(maior)
print(f"{maior} eh o maior")