# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120

import os 
import math

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe um número: "))

factorial = 1

while True:

  if numero == 0:
    print(f"{numero}! = 0")
    break

  elif numero == 1:
    print(f"{numero}! = 1")
    break

  else:
    factorial = math.factorial(numero)
    print(f"{numero}! = {factorial}")
    break
