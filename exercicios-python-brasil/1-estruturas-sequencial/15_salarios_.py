# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_por_hora = float(input("Quando você ganha por hora: "))
horas_trabalhadas_no_mes = float(input("Horas trabahadas no mês: ")) 

salario_bruto = ganho_por_hora * horas_trabalhadas_no_mes
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"Salário Bruto: R${salario_bruto:.0f}")
print(f"Imposto de Renda: R${imposto_de_renda:.0f}")
print(f"INSS: R${inss:.0f}")
print(f"Sindicato: R${sindicato:.0f}")
print(f"Descontos: R${descontos:.0f}")
print(f"Salário Liquido: R${salario_liquido:.0f}")
