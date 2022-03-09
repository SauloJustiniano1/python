# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe o número inteiro: "))

while True:

  if numero == 2 or numero == 3 or numero == 5 or numero == 7:
    print(f"O número primo é {numero}.")
    break

  elif numero == 1 or numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 5 == 0:
    print(f"Esse número não é primo.")
    break

  else:
    print(f"O número primo é {numero}.")
    break
