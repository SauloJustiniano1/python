# 18.1 Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

lista = ""
contador = 0

quantiade_de_numeros = int(input("Informe a quantidade de números no conjunto: "))

while quantiade_de_numeros != contador:
  numero = str(input("Informe um número: "))
  contador = contador + 1
  lista = lista + numero

print(lista)

