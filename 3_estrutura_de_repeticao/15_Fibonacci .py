# 15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

Fibonacci = 1
numero_anterior = 0
numero_posterior = 1
contador = 0

while contador < 50:
  print(Fibonacci, end=" ")
  Fibonacci = numero_anterior + numero_posterior
  numero_anterior = numero_posterior
  numero_posterior = Fibonacci
  contador = contador + 1
