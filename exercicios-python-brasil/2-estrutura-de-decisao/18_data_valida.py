# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0:
  print(f"A data {dia}/{mes}/{ano} é válida.")
else:
  print(f"A data {dia}/{mes}/{ano} é inválida.")
