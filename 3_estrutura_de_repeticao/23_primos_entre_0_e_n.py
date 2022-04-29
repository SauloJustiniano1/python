# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo 
# usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os 
# números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe o número de N: "))

contador = 0

while contador != numero:

  contador = contador + 1
  
  if contador == 1 or contador == 2 or contador == 3 or contador == 5 or contador == 7 or contador % 2 == 0 or contador % 3 == 0 or contador % 5 == 0 or contador % 7 == 0:
    print("Não é primo")
  
  else:
    print("É primo")
