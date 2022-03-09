# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input("Quando você ganha por hora: "))
numero_de_horas = int(input("Números de horas trabalhadas no mês: "))

salario_total = ganho_por_hora * numero_de_horas

print(f"Salário total no referido mês é de R${salario_total:.0f}.")
