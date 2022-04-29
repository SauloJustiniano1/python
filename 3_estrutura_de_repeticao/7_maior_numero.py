# 7. Faça um programa que leia 5 números e informe o maior número.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

contador = maior = 0

while contador < 5:
  numero = int(input("Digite um número: "))
  contador = contador + 1

  if numero > maior:
    maior = numero
  
print(f"O maior número foi {maior}")
