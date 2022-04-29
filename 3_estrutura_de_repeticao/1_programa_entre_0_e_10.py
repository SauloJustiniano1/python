# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja 
# inválido e continue pedindo até que o usuário informe um valor válido.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

nota = int(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
  nota = int(input("Digite uma nota entre 0 e 10: "))

print("Valor válido.")
