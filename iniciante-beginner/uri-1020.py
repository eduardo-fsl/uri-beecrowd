# submissão: 10/08/2021

quantidade_de_dias = int(input())

anos = quantidade_de_dias // 365
anos_resto = quantidade_de_dias % 365

meses = anos_resto // 30
meses_resto = anos_resto % 30

print (f"{anos} ano(s)")
print (f"{meses} mes(es)")
print (f"{meses_resto} dia(s)")