# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

import os 

os.system('cls' if os.name == 'nt' else 'clear')
  
numero_factorial = int(input("Qual é o factorial: "))

numero = numero_factorial

if numero_factorial == 0:
  print(f"{numero}! = 0")

else:
  numero_posterior = numero_factorial - 1

  while numero_posterior != 1:
    numero_factorial = numero_factorial * numero_posterior
    numero_posterior = numero_posterior - 1

print(f"{numero}! = {numero_factorial}")
