# submissão: 23/10/2024

# nc = int(input())
# 
# for i in range(1, nc + 1):
#     n, k = map(int, input().split())
# 
#     sobrevivente = 0
#     for j in range(1, n + 1):
#         sobrevivente = (sobrevivente + k ) % j
#     # print(sobrevivente)
#     print(f"Case {i}: {sobrevivente + 1}")


# submissão: 09/02/2024

# from collections import deque
#
#
# def josephus(n, k):
#     espada = deque(n)
#     while len(espada) > 1:
#         espada.rotate(-k)
#         espada.pop()
#
#     return (espada.pop())
#
#
# nc = int(input())
# for i in range(nc):
#     n, k = map(int, input().split())
#
#     n = [int(j) for j in range(1, 1 + n)]
#
#     josephus_posicao = josephus(n, k)
#
#     print(f"Case {i + 1}: {josephus_posicao}")


# submissão que dá erro de tempo, o algoritmo parece correto mas ele dá erro, acredito que pela limitação da linguagem.
# 06/02/2024

# def jose_recursao(n, k):
#     if n == 1:
#         return 1
#     else:
#         return (jose_recursao(n - 1, k) + k - 1) % n + 1
# 
# 
# nc = int(input())
# for i in range(nc):
#     n, k = map(int, input().split())
# 
#     pessoas = [int(j) for j in range(1, 1 + n)]
# 
#     #     print(f"Case {i+1}: {funcao(lista=pessoas, inicio=0, a=k-1)}")
#     print(f"Case {i + 1}: {jose_recursao(n, k)}")
