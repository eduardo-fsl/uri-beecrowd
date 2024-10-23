numero_funcionario = int(input())
horas_trabalhadas = int(input())
salario_funcionario_por_hora = float(input())

salario_total = horas_trabalhadas * salario_funcionario_por_hora

print (f"NUMBER = {numero_funcionario}")
print (f"SALARY = U$ {salario_total:.2f}")