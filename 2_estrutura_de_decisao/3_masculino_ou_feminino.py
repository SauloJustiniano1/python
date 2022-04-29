# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

valor = input("Digite uma letra (F) ou (M): ")

if valor in ("f", "F"):
  print("Feminino.")

elif valor in ("m", "M"):
  print("Masculino.")

else:
  print("Sexo Inválido.")
