# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais 
# número ele é divisível.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe o número inteiro: "))

while True:

  if numero == 2 or numero == 3 or numero == 5 or numero == 7:
    print(f"O número primo é {numero}.")
    break

  elif numero == 1 or numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
    if numero % 2 == 0:
      print(f"O {numero} é divisível por 2, 4, 6, 8.")
      print(f"Esse número não é primo.")
      break

    elif numero % 3 == 0:
      print(f"O {numero} é divisívrl por 3.")
      print(f"Esse número não é primo.")
      break

    elif numero % 5 == 0:
      print(f"O {numero} é divisível por 5.")
      print(f"Esse número não é primo.")
      break

    elif numero % 7 == 0:
      print(f"O {numero} é divisível por 7.")
      print(f"Esse número não é primo.")
      break

  else:
    print(f"O número primo é {numero}.")
    break
