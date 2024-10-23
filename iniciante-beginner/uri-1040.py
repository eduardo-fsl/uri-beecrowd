# submissão: 26/08/2021

n1, n2, n3, n4 = map(float, input().split())
mediap = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1))/(2 + 3 + 4 + 1)

if mediap >= 7:
    print(f"Media: {mediap:.1f}")
    print("Aluno aprovado.")
if mediap < 5:
    print(f"Media: {mediap:.1f}")
    print("Aluno reprovado.")
if 5 <= mediap <= 6.9:
    print(f"Media: {mediap:.1f}")
    print("Aluno em exame.")
    ne = float(input())
    print(f"Nota do exame: {ne:.1f}")
    medianova = (mediap + ne ) /2
    if medianova >= 5:
            print("Aluno aprovado.")
            print(f"Media final: {medianova:.1f}")
    if medianova < 5:
            print("Aluno reprovado.")
            print(f"Media final: {medianova:.1f}")