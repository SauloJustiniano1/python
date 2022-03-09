# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite mais um número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
  if numero_2 > numero_3:
    print(f"{numero_1}, {numero_2}, {numero_3}.")
  elif numero_2 < numero_3:
    print(f"{numero_1}, {numero_3}, {numero_1}.")

elif numero_2 > numero_1 and numero_2 > numero_3:
  if numero_1 > numero_3:
    print(f"{numero_2}, {numero_1}, {numero_3}.")
  elif numero_1 < numero_3:
    print(f"{numero_2}, {numero_3}, {numero_1}.")

elif numero_3 > numero_1 and numero_3 > numero_2:
  if numero_1 > numero_2:
    print(f"{numero_3}, {numero_1}, {numero_2}.")
  elif numero_1 < numero_2:
    print(f"{numero_3}, {numero_2}, {numero_1}.")
