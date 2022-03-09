# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

lista = []
contador = 0

quantiade_de_numeros = int(input("Informe a quantidade de números no conjunto: "))

while quantiade_de_numeros != contador:
  numero = lista.append(int(input("Informe um número: ")))
  contador = contador + 1

if max(lista) > 1000 or min(lista) < 0:
  print("O valor dos números tem que ser entre 0 e 1000")
else:
  print(f"Conjunto N = {lista}")
  print(f"Valor Maior = {max(lista)}")
  print(f"Valor menor = {min(lista)}")
  print(f"Soma = {max(lista) + min(lista)}")
