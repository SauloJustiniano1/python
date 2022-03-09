# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

lista = []
contador = 0

quantiade_de_numeros = int(input("Informe a quantidade de números no conjunto: "))

while quantiade_de_numeros != contador:
  numero = lista.append(int(input("Informe um número: ")))
  contador = contador + 1

print(f"Conjunto N = {lista}")
print(f"Valor Maior = {max(lista)}")
print(f"Valor menor = {min(lista)}")
print(f"Soma = {max(lista) + min(lista)}")
