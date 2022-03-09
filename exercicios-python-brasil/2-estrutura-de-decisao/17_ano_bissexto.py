# 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe 
# se este ano é ou não bissexto.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

ano = int(input("Informe um determinado ano pra fazer se é ou não bissexto: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f"O ano {ano} é bissexto!")
else:
  print(f"O ano {ano} não é bissexto!")
