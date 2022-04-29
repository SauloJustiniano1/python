# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números 
# pares e a quantidade de números impares.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

contador = par = impar = 0

while contador < 10:
  numero = int(input("Digite um número: "))
  contador = contador + 1
  
  if numero % 2 == 0:
    par = par + 1
  else:
    impar = impar + 1

if par == 0:
  print(f"Não existir números pares.")
  print(f"{impar} números impares.")

elif impar == 0:
  print(f"Não existir números impares.")
  print(f"{par} números pares.") 

else:
  print(f"{par} números pares.")
  print(f"{impar} números impares.")  
