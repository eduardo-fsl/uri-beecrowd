# submissão: 10/09/2021

a, b = map(int, input().split())

if a == b:
    print("O JOGO DUROU 24 HORA(S)")

if a < b:
    print(f"O JOGO DUROU { b -a} HORA(S)")

if a > b:
    print(f"O JOGO DUROU {(24 - a) + b} HORA(S)")
