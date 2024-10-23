#submissão: 10/08/2021

duracao_eventos_segundos = int(input())

horas = duracao_eventos_segundos // 3600
horas_resto = duracao_eventos_segundos % 3600

minutos = horas_resto // 60
minutos_resto = horas_resto % 60

print(f"{horas}:{minutos}:{minutos_resto}")