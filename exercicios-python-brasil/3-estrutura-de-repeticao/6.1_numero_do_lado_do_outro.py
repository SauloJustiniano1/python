# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o 
# programa para que ele mostre os números um ao lado do outro.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = 1

while numero <= 20:
  print(numero, end=" ")
  numero = numero + 1
