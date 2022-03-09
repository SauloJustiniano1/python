# 16. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

Fibonacci = 1
numero_anterior = 0
numero_posterior = 1
contador = 0

while True:
  if Fibonacci <= 500:
    print(Fibonacci, end= " ")
  else:
    break
  Fibonacci = numero_anterior + numero_posterior
  numero_anterior = numero_posterior
  numero_posterior = Fibonacci
  contador = contador + 1
