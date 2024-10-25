# submissão: 03/04/2024

while True:
    n = int(input())
    
    if n == 0:
        break
    
    lista = [int(i) for i in input().split()]
    
    inflexoes = 0
    tamanho_lista = len(lista)
    for i in range(n):
#         if (lista[i-1] < lista[i] > lista[i+1]) or (lista[i-1] > lista[i] < lista[i+1]):
        if i == 0:
            if (lista[n-1] < lista[i] > lista[i+1]) or (lista[n-1] > lista[i] < lista[i+1]):
                inflexoes += 1
        elif i == n - 1:
            if (lista[i-1] < lista[i] > lista[0]) or (lista[i-1] > lista[i] < lista[0]):
                inflexoes += 1
            
        else:
            if (lista[i-1] < lista[i] > lista[i+1]) or (lista[i-1] > lista[i] < lista[i+1]):
                inflexoes += 1
            
    print(inflexoes)
