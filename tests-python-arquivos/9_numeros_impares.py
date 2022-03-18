# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

for c in range(1,50,2):
  print(c, end=" ")
