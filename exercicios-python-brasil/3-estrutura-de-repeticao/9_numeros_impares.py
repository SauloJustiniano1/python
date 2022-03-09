# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = 0
impar = 1

while numero < 50:
  numero = numero + 1

  if numero % 2 != 0:
    impar = numero
    print(impar, end=" ")
