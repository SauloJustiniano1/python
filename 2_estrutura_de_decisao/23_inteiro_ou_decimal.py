# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = float(input("Digite um número: "))

if numero ==  round(numero):
  print(f"O número {int(numero)} é inteiro.")
else:
  print(f"O número {numero} é decimal. ")
