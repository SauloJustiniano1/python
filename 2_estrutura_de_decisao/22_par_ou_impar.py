# 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: 
# utilize o operador módulo (resto da divisão).

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe um número: "))

if numero % 2 == 0:
  print(f"O número {numero} é PAR.")
else:
  print(f"O número {numero} é ÍMPAR.")
