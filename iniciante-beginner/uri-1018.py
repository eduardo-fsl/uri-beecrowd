# submissão: 10/08/2021

valor = int(input())

cedula_100_quantidade = valor // 100
cedula_100_resto = valor % 100

cedula_50_quantidade = cedula_100_resto // 50
cedula_50_resto = cedula_100_resto % 50

cedula_20_quantidade = cedula_50_resto // 20
cedula_20_resto = cedula_50_resto % 20

cedula_10_quantidade = cedula_20_resto // 10
cedula_10_resto = cedula_20_resto % 10

cedula_5_quantidade = cedula_10_resto // 5
cedula_5_resto = cedula_10_resto % 5

cedula_2_quantidade = cedula_5_resto // 2
cedula_2_resto = cedula_5_resto % 2

cedula_1_quantidade = cedula_2_resto // 1
cedula_1_resto = cedula_2_resto % 1

print(valor)
print(f"{cedula_100_quantidade} nota(s) de R$ 100,00")
print(f"{cedula_50_quantidade} nota(s) de R$ 50,00")
print(f"{cedula_20_quantidade} nota(s) de R$ 20,00")
print(f"{cedula_10_quantidade} nota(s) de R$ 10,00")
print(f"{cedula_5_quantidade} nota(s) de R$ 5,00")
print(f"{cedula_2_quantidade} nota(s) de R$ 2,00")
print(f"{cedula_1_quantidade} nota(s) de R$ 1,00")