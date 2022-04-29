# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

letra = str(input("Digite uma letra para saber se é vogal ou consoante: "))

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print("Vogal.")

else:
  print("Consoante.")
  