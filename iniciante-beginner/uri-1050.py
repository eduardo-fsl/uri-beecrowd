# submissão: 21/03/2023

ddd = {
    '61': 'Brasilia',
    '71': 'Salvador',
    '11': 'Sao Paulo',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitoria',
    '31': 'Belo Horizonte',

}

num = input()

if num in ddd:
    print(ddd[num])
else:
    print(f"DDD nao cadastrado")